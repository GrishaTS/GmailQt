import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from functions import (
    PyQtDb,
    base64,
    check_code,
    create_service,
    func_for_form_func_with_arg,
    get_mails,
    matrix_to_line_list,
    os,
    send_code,
    send_mail,
)
from QtDiaologs.create_account import CreateAccount
from QtDiaologs.login_authorization import LoginAutorization
from QtDiaologs.mainwindow import MainW
from QtDiaologs.make_mail import MakeMail
from QtDiaologs.page_html import PageHtml
from QtDiaologs.password_authorization import PasswordAutorization


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        LoginAutorizationWindow.window(self)

    def create_update_account(self):
        info = {
            "code": self.__dict__["code_of_activation"].text(),
            "login": self.__dict__["login_place"].text(),
            "password1": self.__dict__["password1"].text(),
            "password2": self.__dict__["password2"].text(),
        }
        if any([info[i] == "" for i in info]):
            QtWidgets.QMessageBox.warning(
                self, "Ошибка", "Введите все данные", QtWidgets.QMessageBox.Ok
            )
        elif info["password1"] != info["password2"]:
            QtWidgets.QMessageBox.warning(
                self, "Ошибка", "Пароли отличаются", QtWidgets.QMessageBox.Ok
            )
        elif not info["login"].endswith("@gmail.com"):
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                'Почта должна быть в формате "...@gmail.com"',
                QtWidgets.QMessageBox.Ok,
            )
        elif check_code(info["code"], info["login"]):
            PyQtDb().update(
                {"password": info["password1"], "code": ""},
                {"login": info["login"]}
            )
            self.main_window(info["login"])
        else:
            QtWidgets.QMessageBox.warning(
                self, "Ошибка", "Неправильный код", QtWidgets.QMessageBox.Ok
            )

    def check_password(self):
        info = {
            "login": self.label.text()
            .split(
                "Вход в ")[1]
            .split("</p></body>")[0],
            "password": self.password1.text(),
        }
        if list(
            PyQtDb().select(
                where={"login": info["login"], "password": info["password"]}
            )
        ):
            self.main_window(info["login"])
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "Неправильный логин или пароль",
                QtWidgets.QMessageBox.Ok,
            )

    def main_window(self, login):
        theme = list(PyQtDb().select(["theme"], {"login": login}))[0][0]
        MainWindow.window(self, theme, login)


class MainWindow:
    @staticmethod
    def window(self, theme, login):
        self.hide()
        for i in list(self.__dict__):
            try:
                self.__dict__[i].hide()
            except Exception as e:
                print(e)
            del self.__dict__[i]
        self.login = login
        self.theme = theme
        self.flag = True
        self.color_read_background, self.color_unread_background = [
            [QtGui.QColor(255, 255, 255), QtGui.QColor(210, 210, 210)],
            [QtGui.QColor(15, 15, 15), QtGui.QColor(50, 50, 50)],
        ][theme - 1]
        self.color_foreground = [
            QtGui.QColor(0, 0, 0),
            QtGui.QColor(225, 225, 225)
        ][theme - 1]
        styles = [
            [
                'color: rgb(255, 0, 0);\nfont: 11pt "MS Shell Dlg 2";',
                'font: 9pt "MS Shell Dlg 2";',
            ],
            [
                "background-color: rgb(66,133,244);\ncolor:"
                ' rgb(0,0,0);\nfont: 11pt "MS Shell Dlg 2";',
                "background-color: rgb(66,133,244);\ncolor: "
                'rgb(255,255,255);\nfont: 9pt "MS Shell Dlg 2";',
            ],
        ][theme - 1]
        self.selected_style, self.unselected_style = styles
        MainW.setupUi(self, self, theme - 1)
        self.drafts.addItem("Выберите черновик")
        k = 1
        for i in PyQtDb("drafts").select(
            ["snippet", "recipient", "main_text"], {"login": self.login}
        ):
            self.drafts.addItem(
                f"{k}-" + " ".join(f"{i[1]}-{i[0]}-{i[2]}"[:60].split())
            )
            k += 1
        self.drafts.currentIndexChanged.connect(
            func_for_form_func_with_arg(
                MakeMailWindow.return_to_draft,
                self,
                theme,
            )
        )
        self.classic_theme.toggled.connect(
            func_for_form_func_with_arg(MainWindow.window, self, 1, login)
        )
        self.dark_theme.toggled.connect(
            func_for_form_func_with_arg(MainWindow.window, self, 2, login)
        )
        self.make_mail.clicked.connect(
            func_for_form_func_with_arg(
                MakeMailWindow.window,
                self,
                login,
                theme,
            )
        )
        self.update.clicked.connect(
            func_for_form_func_with_arg(MainWindow.update_func, self)
        )
        self.search.clicked.connect(
            func_for_form_func_with_arg(
                MainWindow.display_mails_func, self, MainWindow.searche_func
            )
        )
        self.all_mail.clicked.connect(
            func_for_form_func_with_arg(
                MainWindow.display_mails_func, self, MainWindow.all_mail_func
            )
        )
        self.incoming.clicked.connect(
            func_for_form_func_with_arg(
                MainWindow.display_mails_func, self, MainWindow.incoming_func
            )
        )
        self.sent.clicked.connect(
            func_for_form_func_with_arg(
                MainWindow.display_mails_func, self, MainWindow.sent_func
            )
        )
        self.list_of_mails.clicked.connect(
            func_for_form_func_with_arg(MainWindow.display_mail, self)
        )
        MainWindow.display_mails_func(self, MainWindow.all_mail_func)

    @staticmethod
    def take_new_letters(self, page=None):
        letters = PyQtDb("letters")
        if self.flag:
            try:
                requests.head("http://www.google.com/", timeout=1)
            except requests.ConnectionError:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Ошибка",
                    "Нет подключения к сети",
                    QtWidgets.QMessageBox.Ok,
                )
            self.flag = False
        if not self.flag:
            try:
                for info in get_mails(self.login, page=None):
                    info["login"] = self.login
                    letters += info
            except Exception as e:
                print(e)

    @staticmethod
    def display_mail(self):
        mail = self.list_of_mails.item(
            self.list_of_mails.currentRow(),
            0
        ).text()
        from_ = mail.split("---")[0]
        to_ = mail.split("---")[1]
        date = mail.split("---")[2].split("\n")[0]
        text_of_mail = list(
            PyQtDb("letters").select(
                ["text"], like={"from_": from_, "to_": to_, "date": date}
            )
        )[0][0]
        id_of_mail = list(
            PyQtDb("letters").select(
                ["id_of_letter"],
                like={"from_": from_, "to_": to_, "date": date}
            )
        )[0][0]
        text_of_parts_mail = matrix_to_line_list(eval(text_of_mail))
        try:
            PageHtmlWindow.window(
                self,
                list(text_of_parts_mail),
                id_of_mail,
                self.login,
                self.theme,
            )
        except Exception as e:
            print(e)

    @staticmethod
    def update_func(self):
        try:
            requests.head("http://www.google.com/", timeout=1)
            MainWindow.take_new_letters(self)
            MainWindow.display_mails_func(self, MainWindow.all_mail_func)
        except requests.ConnectionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "Нет подключения к сети",
                QtWidgets.QMessageBox.Ok
            )

    @staticmethod
    def searche_func(self):
        text_for_search = self.search_text.text()
        text_for_search = PyQtDb.replace({"text_for_search": text_for_search})[
            "text_for_search"
        ]
        for i in PyQtDb("letters").execute(
            f"SELECT from_, to_, snippet, date, read FROM letters WHERE"
            f' "login" = "{self.login}" and ("to_" LIKE'
            f' "%{text_for_search}%" or "from_" LIKE "%{text_for_search}%"'
            f' or "snippet" LIKE "%{text_for_search}%"'
            f'or "text" LIKE "%{text_for_search}%")'
        ):
            yield tuple(
                j.replace("⋽", '"').replace("⋵", "\\") if type(j) is str else j
                for j in i
            )

    @staticmethod
    def display_mails_func(self, ordering):
        item = self.list_of_mails.horizontalHeaderItem(0)
        if ordering is MainWindow.searche_func:
            item.setText("Поиск")
        elif ordering is MainWindow.all_mail_func:
            item.setText("Вся почта")
        elif ordering is MainWindow.incoming_func:
            item.setText("Входящие")
        elif ordering is MainWindow.sent_func:
            item.setText("Исходящие")
        MainWindow.take_new_letters(self)
        generator = ordering(self)
        letters_on_display = []
        for _ in range(100):
            try:
                letters_on_display.append(next(generator))
            except StopIteration:
                break
        letters_on_display = sorted(
            letters_on_display, key=lambda x: x[3], reverse=True
        )
        ans = []
        for x in letters_on_display:
            snippet = " ".join(x[2].split())[:100]
            snippet = f"{x[0]}---{x[1]}---{x[3]}\n{snippet}".strip()
            ans.append((snippet, x[4]))
        self.list_of_mails.setRowCount(0)
        for i, row in enumerate(ans):
            self.list_of_mails.setRowCount(self.list_of_mails.rowCount() + 1)
            item_for_table = QtWidgets.QTableWidgetItem(row[0])
            item_for_table.setFlags(QtCore.Qt.ItemIsEnabled)
            self.list_of_mails.setItem(i, 0, item_for_table)
            if row[1] == "False":
                MainWindow.color_row(
                    self,
                    i,
                    self.color_unread_background,
                    self.color_foreground,
                )
            else:
                MainWindow.color_row(
                    self,
                    i,
                    self.color_read_background,
                    self.color_foreground,
                )
        self.list_of_mails.resizeRowsToContents()
        self.list_of_mails.resizeColumnsToContents()
        self.show()

    @staticmethod
    def color_row(self, row, back, fore):
        for i in range(self.list_of_mails.columnCount()):
            self.list_of_mails.item(row, i).setBackground(back)
            self.list_of_mails.item(row, i).setForeground(fore)

    @staticmethod
    def all_mail_func(self):
        self.all_mail.setStyleSheet(self.selected_style)
        self.incoming.setStyleSheet(self.unselected_style)
        self.sent.setStyleSheet(self.unselected_style)
        return PyQtDb("letters").select(
            ["from_", "to_", "snippet", "date", "read"], {"login": self.login}
        )

    @staticmethod
    def incoming_func(self):
        self.all_mail.setStyleSheet(self.unselected_style)
        self.incoming.setStyleSheet(self.selected_style)
        self.sent.setStyleSheet(self.unselected_style)
        return PyQtDb("letters").execute(
            f"SELECT from_, to_, snippet, date, read FROM letters WHERE"
            f' "login" = "{self.login}" and ("to_" LIKE "%{self.login}%" or '
            f'("from_" NOT LIKE "%{self.login}%" '
            f'and "to_" NOT LIKE "%{self.login}%"))'
        )

    @staticmethod
    def sent_func(self):
        self.all_mail.setStyleSheet(self.unselected_style)
        self.incoming.setStyleSheet(self.unselected_style)
        self.sent.setStyleSheet(self.selected_style)
        return PyQtDb("letters").select(
            ["from_", "to_", "snippet", "date", "read"],
            {"login": self.login},
            {"from_": f"%{self.login}%"},
        )


class MakeMailWindow:
    @staticmethod
    def window(self, login, theme, draft=None):
        self.hide()
        for i in list(self.__dict__):
            try:
                self.__dict__[i].hide()
            except Exception as e:
                print(e)
            del self.__dict__[i]
        self.login = login
        self.theme = theme
        MakeMail.setupUi(self, self)
        if draft:
            self.snippet.setText(draft[0])
            self.recipient.setText(draft[1])
            self.main_text.setText(draft[2])
            PyQtDb("drafts").delete(
                {
                    "snippet": draft[0],
                    "recipient": draft[1],
                    "main_text": draft[2],
                }
            )
        self.send.clicked.connect(
            func_for_form_func_with_arg(MakeMailWindow.send_func, self)
        )
        self.attach.clicked.connect(
            func_for_form_func_with_arg(MakeMailWindow.attach_func, self)
        )
        self.draft.clicked.connect(
            func_for_form_func_with_arg(MakeMailWindow.draft_func, self)
        )
        self.back.clicked.connect(
            func_for_form_func_with_arg(MakeMailWindow.back_func, self)
        )
        self.show()

    @staticmethod
    def return_to_draft(self, theme):
        drafts_of_login = list(
            PyQtDb("drafts").select(
                ["snippet", "recipient", "main_text"], {"login": self.login}
            )
        )
        draft = drafts_of_login[
            int(self.drafts.currentText().split("-")[0]) - 1
        ]
        MakeMailWindow.window(self, self.login, theme, draft)

    @staticmethod
    def send_func(self):
        while True:
            try:
                requests.head("http://www.google.com/", timeout=1)
                snippet = self.snippet.text()
                recipient = self.recipient.toPlainText()
                main_text = self.main_text.toPlainText()
                files = list(
                    set(
                        open(f"files/{self.login}/files.txt", "r")
                        .read()
                        .strip()
                        .split()
                    )
                )
                if any([i == "" for i in [snippet, recipient, main_text]]):
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Ошибка",
                        "Обязательно ввести первые три пункта!",
                        QtWidgets.QMessageBox.Ok,
                    )

                else:
                    send_mail(self.login, snippet, recipient, main_text, files)
                    with open(f"files/{self.login}/files.txt", "w"):
                        ...
                    MainWindow.window(self, self.theme, self.login)
                break
            except requests.ConnectionError:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Ошибка",
                    "Нет подключения к сети",
                    QtWidgets.QMessageBox.Ok,
                )
                break

    @staticmethod
    def attach_func(self):
        f_name = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
        )[0]
        with open(f"files/{self.login}/files.txt", "a") as f:
            f.write(f"{f_name}\n")
        self.files.setPlainText(
            self.files.toPlainText() + f'{f_name.split("/")[-1]}\n'
        )

    @staticmethod
    def draft_func(self):
        recipient = self.recipient.toPlainText()
        snippet = self.snippet.text()
        main_text = self.main_text.toPlainText()
        if any([recipient, snippet, main_text]):
            drafts = PyQtDb("drafts")
            drafts += {
                "main_text": main_text,
                "recipient": recipient,
                "snippet": snippet,
                "login": self.login,
            }
        MainWindow.window(self, self.theme, self.login)

    @staticmethod
    def back_func(self):
        MainWindow.window(self, self.theme, self.login)


class LoginAutorizationWindow:
    @staticmethod
    def window(self):
        self.hide()
        for i in list(self.__dict__):
            self.__dict__[i].hide()
            del self.__dict__[i]
        LoginAutorization.setupUi(self, self)
        self.create_an_account.clicked.connect(
            func_for_form_func_with_arg(CreateAccountWindow.window, self)
        )
        self.resume.clicked.connect(
            func_for_form_func_with_arg(
                PasswordAuthorizationWindow.window,
                self
            )
        )
        self.forget_password.clicked.connect(
            func_for_form_func_with_arg(UpdatePasswordWindow.window, self)
        )
        self.show()


class PasswordAuthorizationWindow:
    @staticmethod
    def window(self):
        login = self.login_place.text()
        if not login.endswith("@gmail.com"):
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                'Почта должна быть в формате "...@gmail.com"',
                QtWidgets.QMessageBox.Ok,
            )
        else:
            self.hide()
            for i in list(self.__dict__):
                self.__dict__[i].hide()
                del self.__dict__[i]
            PasswordAutorization.setupUi(self, self)
            self.to_login.clicked.connect(
                func_for_form_func_with_arg(
                    LoginAutorizationWindow.window,
                    self,
                )
            )
            self.label.setText(
                f"<html><head/><body>"
                f'<p align="center">Вход в {login}</p></body></html>'
            )
            self.resume.clicked.connect(self.check_password)
            self.forget_password.clicked.connect(
                func_for_form_func_with_arg(UpdatePasswordWindow.window, self)
            )
            self.show()


class CreateAccountWindow:
    @staticmethod
    def window(self):
        self.hide()
        for i in list(self.__dict__):
            self.__dict__[i].hide()
            del self.__dict__[i]
        CreateAccount.setupUi(self, self)
        self.have_account.clicked.connect(
            func_for_form_func_with_arg(LoginAutorizationWindow.window, self)
        )
        self.resume.clicked.connect(self.create_update_account)
        self.send_code.clicked.connect(
            func_for_form_func_with_arg(CreateAccountWindow.check_login, self)
        )
        self.show()

    @staticmethod
    def check_login(self):
        login = self.login_place.text()
        if not list(PyQtDb().select(where={"login": login})):
            while True:
                try:
                    requests.head("http://www.google.com/", timeout=1)
                    break
                except requests.ConnectionError:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Ошибка",
                        "Нет подключения к сети",
                        QtWidgets.QMessageBox.Ok,
                    )
            send_code(self)
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "Уже есть аккаунт с этим логином",
                QtWidgets.QMessageBox.Ok,
            )


class UpdatePasswordWindow:
    @staticmethod
    def window(self):
        self.hide()
        for i in list(self.__dict__):
            self.__dict__[i].hide()
            del self.__dict__[i]
        CreateAccount.setupUi(self, self)
        self.label_5.setText(" Восстановление пароля")
        self.have_account.clicked.connect(
            func_for_form_func_with_arg(LoginAutorizationWindow.window, self)
        )
        self.send_code.clicked.connect(
            func_for_form_func_with_arg(UpdatePasswordWindow.check_login, self)
        )
        self.resume.clicked.connect(self.create_update_account)
        self.show()

    @staticmethod
    def check_login(self):
        login = self.login_place.text()
        if list(PyQtDb().select(where={"login": login})):
            while True:
                try:
                    requests.head("http://www.google.com/", timeout=1)
                    break
                except requests.ConnectionError:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Ошибка",
                        "Нет подключения к сети",
                        QtWidgets.QMessageBox.Ok,
                    )
            send_code(self)
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Ошибка",
                "Аккаунта с этим логином нет",
                QtWidgets.QMessageBox.Ok,
            )


class PageHtmlWindow:
    @staticmethod
    def window(self, text_of_parts_mail, id_of_mail, login, theme):
        self.hide()
        for i in list(self.__dict__):
            try:
                self.__dict__[i].hide()
            except Exception as e:
                print(e)
            del self.__dict__[i]
        PageHtml.setupUi(self, self)
        self.id_of_mail = id_of_mail
        self.attach = eval(
            list(PyQtDb("letters").select(
                ["files"],
                {"id_of_letter": id_of_mail}
            ))[0][0],
        )
        if self.attach:
            self.files.setPlainText("\n".join([i[0] for i in self.attach]))
        else:
            self.save_att.hide()
            self.files.setPlainText("Нет приложенных файлов")
        self.html_area.setHtml(text_of_parts_mail[0][0])
        self.login = login
        self.theme = theme
        if len(text_of_parts_mail) == 1:
            self.resume.clicked.connect(
                func_for_form_func_with_arg(
                    MainWindow.window,
                    self,
                    theme,
                    login
                )
            )
        else:
            self.resume.clicked.connect(
                func_for_form_func_with_arg(
                    PageHtmlWindow.next_page, self, text_of_parts_mail[1:]
                )
            )
        self.save_att.clicked.connect(
            func_for_form_func_with_arg(PageHtmlWindow.save_files, self)
        )
        self.show()

    @staticmethod
    def next_page(self, text_of_parts_mail):
        self.html_area.setHtml(text_of_parts_mail[0][0])
        if len(text_of_parts_mail) == 1:
            self.resume.clicked.connect(
                func_for_form_func_with_arg(
                    MainWindow.window, self, self.theme, self.login
                )
            )
        else:
            self.resume.clicked.connect(
                func_for_form_func_with_arg(
                    PageHtmlWindow.next_page, self, text_of_parts_mail[1:]
                )
            )

    @staticmethod
    def save_files(self):
        path = QFileDialog.getExistingDirectory(
            self, "Выберите путь", f"C:\\Users\\{os.getlogin()}"
        )
        service = create_service(self.login)
        for i in self.attach:
            try:
                att = service.users().messages().attachments().get(
                    userId="me",
                    messageId=self.id_of_mail,
                    id=i[1].strip()
                ).execute()
                data = att["data"]
                file_data = base64.urlsafe_b64decode(data.encode("UTF-8"))
                with open(path + f"/{i[0]}", "wb") as f:
                    f.write(file_data)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
