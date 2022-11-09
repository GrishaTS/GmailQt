from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class PageHtml(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(490, 540)
        Dialog.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.save_att = QtWidgets.QPushButton(Dialog)
        self.save_att.setGeometry(QtCore.QRect(10, 490, 41, 41))
        self.save_att.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\nbackground-color: rgb(185, 185, 185);\nfont: 75 26pt \"MS Shell Dlg 2\";")
        self.save_att.setObjectName("save_att")
        self.html_area = QWebEngineView(Dialog)
        self.html_area.setGeometry(QtCore.QRect(10, 10, 471, 471))
        self.html_area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.html_area.setObjectName("html_area")
        self.resume = QtWidgets.QPushButton(Dialog)
        self.resume.setGeometry(QtCore.QRect(410, 490, 71, 41))
        self.resume.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\nbackground-color: rgb(185, 185, 185);")
        self.resume.setObjectName("resume")
        self.files = QtWidgets.QTextEdit(Dialog)
        self.files.setGeometry(QtCore.QRect(60, 490, 201, 41))
        self.files.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.files.setObjectName("files")
        self.files.setReadOnly(True)
        PageHtml.retranslateUi(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.save_att.setText(_translate("Dialog", "⤓"))
        self.resume.setText(_translate("Dialog", "Далее"))
