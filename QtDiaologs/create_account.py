from PyQt5 import QtCore, QtGui, QtWidgets


class CreateAccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(300, 300)
        self.login_place = QtWidgets.QLineEdit(Dialog)
        self.login_place.setGeometry(QtCore.QRect(10, 120, 281, 21))
        self.login_place.setObjectName("login_place")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.have_account = QtWidgets.QPushButton(Dialog)
        self.have_account.setGeometry(QtCore.QRect(10, 260, 101, 23))
        self.have_account.setStyleSheet("color: rgb(0, 85, 255);")
        self.have_account.setObjectName("pushButton_2")
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
        self.password1 = QtWidgets.QLineEdit(Dialog)
        self.password1.setGeometry(QtCore.QRect(10, 180, 131, 21))
        self.password1.setObjectName("password1")
        self.password2 = QtWidgets.QLineEdit(Dialog)
        self.password2.setGeometry(QtCore.QRect(160, 180, 131, 21))
        self.password2.setObjectName("password2")
        self.password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 50, 231, 31))
        self.label_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.send_code = QtWidgets.QPushButton(Dialog)
        self.send_code.setGeometry(QtCore.QRect(10, 150, 131, 23))
        self.send_code.setObjectName("send_code")
        self.code_of_activation = QtWidgets.QLineEdit(Dialog)
        self.code_of_activation.setGeometry(QtCore.QRect(160, 150, 131, 20))
        self.code_of_activation.setObjectName("code_of_activation")

        CreateAccount.retranslateUi(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_place.setPlaceholderText(_translate("Dialog", "Адрес эл. почты                                     "
                                                                 "     (@gmail.com)"))
        self.label_2.setText(_translate("Dialog", " Перейти в  Gmail"))
        self.have_account.setText(_translate("Dialog", "Войти"))
        self.resume.setText(_translate("Dialog", "Далее"))
        self.label_3.setText(_translate("Dialog", "G"))
        self.label_4.setText(_translate("Dialog", "o"))
        self.label_6.setText(_translate("Dialog", "o"))
        self.label_7.setText(_translate("Dialog", " l"))
        self.label_8.setText(_translate("Dialog", "  e"))
        self.label_9.setText(_translate("Dialog", "g"))
        self.password1.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.password2.setPlaceholderText(_translate("Dialog", "Подтвердите пароль"))
        self.label_5.setText(_translate("Dialog", "Создайте аккаунт Google"))
        self.send_code.setText(_translate("Dialog", "Отправить код"))
        self.code_of_activation.setPlaceholderText(_translate("Dialog", "Код активации"))