from PyQt5 import QtCore, QtGui, QtWidgets


class MakeMail(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(539, 467)
        Dialog.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.recipient = QtWidgets.QTextEdit(Dialog)
        self.recipient.setGeometry(QtCore.QRect(0, 40, 541, 41))
        self.recipient.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 10pt;")
        self.recipient.setObjectName("recipient")
        self.snippet = QtWidgets.QLineEdit(Dialog)
        self.snippet.setGeometry(QtCore.QRect(0, 80, 541, 41))
        self.snippet.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 10pt;")
        self.snippet.setMaxLength(100)
        self.snippet.setObjectName("snippet")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\nfont: 12pt \"MS Shell Dlg 2\";\nbackground-color: rgb(60, 60, 60)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 406, 541, 61))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.send = QtWidgets.QPushButton(Dialog)
        self.send.setGeometry(QtCore.QRect(0, 420, 121, 41))
        self.send.setStyleSheet("color: rgb(255, 255, 255);\nfont: 12pt \"MS Shell Dlg 2\";\nbackground-color: rgb(13, 119, 212);")
        self.send.setObjectName("send")
        self.attach = QtWidgets.QPushButton(Dialog)
        self.attach.setGeometry(QtCore.QRect(150, 420, 41, 41))
        self.attach.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\nbackground-color: rgb(255, 255, 255);")
        self.attach.setObjectName("attach")
        self.draft = QtWidgets.QPushButton(Dialog)
        self.draft.setGeometry(QtCore.QRect(490, 420, 41, 41))
        self.draft.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 14pt \"MS Shell Dlg 2\";")
        self.draft.setObjectName("draft")
        self.files = QtWidgets.QTextEdit(Dialog)
        self.files.setGeometry(QtCore.QRect(200, 420, 201, 41))
        self.files.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.files.setObjectName("files")
        self.files.setReadOnly(True)
        self.main_text = QtWidgets.QTextEdit(Dialog)
        self.main_text.setGeometry(QtCore.QRect(0, 120, 541, 291))
        self.main_text.setStyleSheet("background-color: rgb(255, 255, 255);\nfont: 10pt;")
        self.main_text.setObjectName("main_text")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(440, 420, 41, 41))
        self.back.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\nbackground-color: rgb(255, 255, 255);")
        self.back.setObjectName("back")
        MakeMail.retranslateUi(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Новое сообщение"))
        self.recipient.setPlaceholderText(_translate("Dialog", "Получатели (каждый новый с новой строки)"))
        self.send.setText(_translate("Dialog", "Отправить"))
        self.snippet.setPlaceholderText(_translate("Dialog", "Тема"))
        self.main_text.setPlaceholderText(_translate("Dialog", "Текст"))
        self.files.setPlaceholderText(_translate("Dialog", "Файлы"))
        self.attach.setText(_translate("Dialog", "📎"))
        self.draft.setText(_translate("Dialog", "🗑"))
        self.back.setText(_translate("Dialog", "🔙"))
