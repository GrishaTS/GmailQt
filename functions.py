from __future__ import print_function

import base64
import datetime
import email
import os
import os.path
import pickle
import random
import sqlite3
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRET_FILE = "credentials.json"
SCOPES = ["https://mail.google.com/"]


def func_for_form_func_with_arg(func, *args, **kwargs):
    def new_f():
        func(*args, **kwargs)

    return new_f


def dec(func):
    def new(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} --- {e}")

    return new


def matrix_to_line_list(lis):
    for item in lis:
        if type(item) is list:
            for x in matrix_to_line_list(item):
                yield x
        else:
            yield item


@dec
def send_mail(login, snippet, recipient, main_text, files):
    service = create_service(login)
    bad_request = []
    for i in recipient.split():
        try:
            mime_message = MIMEMultipart()
            mime_message["to"] = i.strip()
            mime_message["subject"] = snippet
            mime_message.attach(MIMEText(main_text, "plain"))
            if files:
                for f in files:
                    with open(f, "rb") as file:
                        part = MIMEApplication(
                            file.read(),
                            Name=f.split("/")[-1]
                        )
                    part["Content-Disposition"] = (
                        'attachment; filename="%s"' % f.split("/")[-1]
                    )
                    mime_message.attach(part)
            raw_string = base64.urlsafe_b64encode(mime_message.as_bytes())
            raw_string = raw_string.decode()
            service.users().messages().send(
                userId="me", body={"raw": raw_string}
            ).execute()
        except Exception as e:
            print(e)
            bad_request.append(i)
    print(bad_request)


@dec
def create_service(login):
    pickle_file = f"files/{login}/token{login}.pickle"
    cred = None
    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as token:
            cred = pickle.load(token)
    else:
        os.makedirs(f"files/{login}")
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                SCOPES,
            )
            cred = flow.run_local_server()
        with open(pickle_file, "wb") as token:
            pickle.dump(cred, token)
    service = build("gmail", "v1", credentials=cred)
    return service


@dec
def check_code(code_of_activation, login):
    return list(PyQtDb().select(
        ["code"],
        {"login": login})
    ) == [(code_of_activation,)]


@dec
def send_code(self):
    login = self.login_place.text()
    db = PyQtDb()
    if not list(db.select(where={"login": login})):
        db += {"login": login}
    service = create_service(login)
    code = random.randint(10000, 99999)
    db.update({"code": code}, {"login": login})
    email_msg = f"Ваш код: {code}"
    mime_message = MIMEMultipart()
    mime_message["to"] = login
    mime_message["subject"] = "Код"
    mime_message.attach(MIMEText(email_msg, "plain"))
    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw_string})
    service.execute()


def maildate_to_datetime(mail_date):
    t = " ".join(mail_date.split(", ")[1].split()[:4])
    try:
        t = time.strptime(t, "%d %b %Y %X")
    except Exception as e:
        print(e)
        t = time.strptime(t, "0%d %b %Y %X")
    t = datetime.datetime(
        year=t.tm_year,
        month=t.tm_mon,
        day=t.tm_mday,
        hour=t.tm_hour,
        minute=t.tm_min,
        second=t.tm_sec,
    )
    try:
        try:
            time_z = mail_date.split("+")[1].split()[0][:2]
            t -= datetime.timedelta(hours=int(time_z))
        except Exception as e:
            print(e)
            time_z = mail_date.split("-")[1].split()[0][:2]
            t += datetime.timedelta(hours=int(time_z))
        t += datetime.timedelta(hours=3)
    except Exception as e:
        print(e)
        ...
    return t


def take_files_from_mail(mail):
    ans = []
    if "parts" in mail and type(mail) is dict:
        for j in mail["parts"]:
            if j["filename"]:
                ans.append((j["filename"], j["body"]["attachmentId"]))
    else:
        if mail["filename"]:
            ans.append((mail["filename"], mail["body"]["attachmentId"]))
    return ans


def take_text_from_parts(mail):
    ans = []
    for j in mail["parts"]:
        if "parts" in j:
            ans += take_text_from_parts(j)
        if not j.get("filename", ""):
            try:
                msg_str = base64.urlsafe_b64decode(
                    j["body"]["data"].encode("UTF8")
                )
                mime_msg = email.message_from_string(msg_str.decode("utf8"))
                type_of_text = [
                    "text/plain",
                    "text/html",
                    "multipart/related",
                    "multipart/alternative",
                ].index(j.get("mimeType", ""))
            except Exception as e:
                print(e)
                continue
            ans.append((str(mime_msg), type_of_text))
    return ans


def take_text_from_mail(mail):
    ans = []
    if "parts" in mail and type(mail) is dict:
        ans += [take_text_from_parts(mail)]
    else:
        ans += [take_text_from_parts({"parts": [mail]})]
    return ans


@dec
def get_mails(login, page=None):
    service = create_service(login)
    results = (
        service.users()
        .messages()
        .list(
            userId="me",
        )
        .execute()
    )
    letters = PyQtDb("letters")
    for i in results["messages"]:
        if not list(letters.select(where={"id_of_letter": i["id"]})):
            all_mail = service.users().messages().get(userId="me", id=i["id"])
            all_mail = all_mail.execute()
            mail = all_mail["payload"]
            try:
                ans = {
                    "from_": [
                        j["value"]
                        for j in mail["headers"]
                        if j["name"].lower() == "from"
                    ][0],
                    "to_": [
                        j["value"] for j in mail["headers"]
                        if j["name"].lower() == "to"
                    ][0],
                    "date": maildate_to_datetime(
                        [
                            j["value"]
                            for j in mail["headers"]
                            if j["name"].lower() == "date"
                        ][0]
                    ),
                    "text": take_text_from_mail(mail),
                    "files": take_files_from_mail(mail),
                    "read": not ("UNREAD" in all_mail["labelIds"]),
                    "snippet": all_mail.get("snippet", ""),
                    "id_of_letter": all_mail["id"],
                }
                if login == ans["from_"]:
                    ans["read"] = True
                if ans["snippet"] == "":
                    ans["snippet"] = "Без темы"
                yield ans
            except Exception as e:
                print(e)
                ...


class PyQtDb:
    """временное решение
    из=за того что sqlite не берет строки
    в которых имеются знаки " и \\, я на время
    хранения их в бд, меняю по следующему принципу

    " -> ⋽
    \\ -> ⋵

    """

    def __init__(self, table="authorization"):
        self.table = table

    @staticmethod
    def replace(arg):
        if not arg:
            return {}
        arg = {str(i).replace('"', "⋽"): str(arg[i]).replace('"', "⋽")
               for i in arg}
        return {str(i).replace("\\", "⋵"): str(arg[i]).replace("\\", "⋵")
                for i in arg}

    def __iadd__(self, args):
        args = PyQtDb.replace(args)
        with sqlite3.connect("db.sqlite") as db:
            db.execute(
                f"""INSERT INTO {self.table} ("{'", "'.join([str(i)
                                                             for i in args])}")
                 VALUES ("{'", "'.join([str(args[i]) for i in args])}");"""
            )
            db.commit()
        return self

    def select(self, take=None, where=None, like=None, not_like=None):
        where = PyQtDb.replace(where)
        like = PyQtDb.replace(like)
        not_like = PyQtDb.replace(not_like)
        select_text = "SELECT"
        if take:
            select_text += f' {", ".join(take)}'
        else:
            select_text += " *"
        select_text += f" FROM {self.table}"
        if any([where, like, not_like]):
            select_text += " WHERE "
        if where:
            select_text += " and ".join([f'"{i}" = "{where[i]}"'
                                         for i in where])
        if like:
            if where:
                select_text += " and "
            select_text += " and ".join([f'"{i}" LIKE "{like[i]}"'
                                         for i in like])
        if not_like:
            if any([where, like]):
                select_text += " and "
            select_text += " and ".join(
                [f'"{i}" NOT LIKE "{not_like[i]}"' for i in not_like]
            )
        select_text += ";"
        with sqlite3.connect("db.sqlite") as db:
            for i in db.execute(select_text):
                yield tuple(
                    j.replace("⋽", '"').replace("⋵", "\\") if type(j) is str
                    else j for j in i
                )

    def update(self, upd, where=None):
        where = PyQtDb.replace(where)
        upd = PyQtDb.replace(upd)
        with sqlite3.connect("db.sqlite") as db:
            if where:
                db.execute(
                    f"""UPDATE {self.table} SET
                     {', '.join([f'"{i}" = "{upd[i]}"' for i in upd])} WHERE
                     {' and '.join([f'{i} = "{where[i]}"' for i in where])};"""
                )
            else:
                db.execute(
                    f"""UPDATE {self.table} SET
                     {', '.join([f'"{i}" = "{upd[i]}"' for i in upd])};"""
                )
            db.commit()

    def execute(self, execu):
        with sqlite3.connect("db.sqlite") as db:
            ans = db.execute(execu)
        if ans:
            return ans

    def delete(self, where=None):
        where = PyQtDb.replace(where)
        with sqlite3.connect("db.sqlite") as db:
            if where:
                db.execute(
                    f"DELETE from {self.table} where "
                    + " and ".join([f'"{i}" = "{where[i]}"' for i in where])
                    + ";"
                )
            else:
                db.execute(f"DELETE from {self.table};")
            db.commit()
