from PyQt5 import QtCore, QtWidgets


class LoginAutorization(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(300, 300)
        self.login_place = QtWidgets.QLineEdit(Dialog)
        self.login_place.setGeometry(QtCore.QRect(50, 130, 201, 31))
        self.login_place.setObjectName("login_place")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 60, 51, 21))
        self.label.setStyleSheet("font: 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.forget_password = QtWidgets.QPushButton(Dialog)
        self.forget_password.setGeometry(QtCore.QRect(50, 170, 101, 21))
        self.forget_password.setStyleSheet("color: rgb(0, 85, 255);\nfont: 75 8pt \"MS Shell Dlg 2\";")
        self.forget_password.setObjectName("forget_password")
        self.create_an_account = QtWidgets.QPushButton(Dialog)
        self.create_an_account.setGeometry(QtCore.QRect(10, 260, 101, 23))
        self.create_an_account.setStyleSheet("color: rgb(0, 85, 255);")
        self.create_an_account.setObjectName("create_an_account")
        self.resume = QtWidgets.QPushButton(Dialog)
        self.resume.setGeometry(QtCore.QRect(190, 230, 75, 31))
        self.resume.setStyleSheet("font: 75 12pt \"Leelawadee UI\";\nbackground-color: rgb(25, 86, 255);\ncolor: rgb(255, 255, 255);")
        self.resume.setObjectName("resume")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 21, 21))
        self.label_3.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(66, 133, 244);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(145, 20, 21, 21))
        self.label_4.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(255, 10, 10);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(129, 20, 21, 21))
        self.label_6.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(255, 163, 35);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(169, 10, 31, 41))
        self.label_7.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(0, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(170, 20, 41, 21))
        self.label_8.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(255, 10, 10);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(160, 10, 21, 41))
        self.label_9.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\ncolor: rgb(66, 133, 244);")
        self.label_9.setObjectName("label_9")
        LoginAutorization.retranslateUi(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Логин"))
        self.login_place.setPlaceholderText(_translate("Dialog", "Адрес эл. почты              (@gmail.com)"))
        self.label.setText(_translate("Dialog", "Вход"))
        self.forget_password.setText(_translate("Dialog", "Забыли пароль?"))
        self.create_an_account.setText(_translate("Dialog", "Создать аккаунт"))
        self.resume.setText(_translate("Dialog", "Далее"))
        self.label_2.setText(_translate("Dialog", " Перейти в  Gmail"))
        self.label_3.setText(_translate("Dialog", "G"))
        self.label_4.setText(_translate("Dialog", "o"))
        self.label_6.setText(_translate("Dialog", "o"))
        self.label_7.setText(_translate("Dialog", " l"))
        self.label_8.setText(_translate("Dialog", "  e"))
        self.label_9.setText(_translate("Dialog", "g"))
