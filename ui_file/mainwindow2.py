from PyQt5 import QtCore, QtGui, QtWidgets


class MainW2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(983, 613)
        Dialog.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.list_of_mails = QtWidgets.QListView(Dialog)
        self.list_of_mails.setGeometry(QtCore.QRect(180, 70, 791, 541))
        self.list_of_mails.setObjectName("list_of_mails")
        self.make_mail = QtWidgets.QPushButton(Dialog)
        self.make_mail.setGeometry(QtCore.QRect(10, 80, 111, 41))
        self.make_mail.setStyleSheet('color: rgb(255, 255, 255);\nfont: 11pt "MS Shell Dlg 2";\nbackground-color: rgb(197,34,30);')
        self.make_mail.setObjectName("make_mail")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(130, 80, 41, 41))
        self.update.setStyleSheet('font: 14pt "MS Shell Dlg 2";\nbackground-color: rgb(251,188,4);\ncolor: rgb(0, 0, 0);')
        self.update.setObjectName("update")
        self.forward = QtWidgets.QPushButton(Dialog)
        self.forward.setGeometry(QtCore.QRect(950, 20, 21, 23))
        self.forward.setStyleSheet('font: 14pt "MS Shell Dlg 2";\nbackground-color: rgb(197,34,30);\ncolor: rgb(255, 255, 255);')
        self.forward.setObjectName("forward")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(920, 20, 21, 23))
        self.back.setStyleSheet('font: 14pt "MS Shell Dlg 2";\nbackground-color: rgb(197,34,30);\ncolor: rgb(255, 255, 255);')
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(840, 20, 61, 20))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\ncolor: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.search_text = QtWidgets.QLineEdit(Dialog)
        self.search_text.setGeometry(QtCore.QRect(182, 10, 571, 41))
        self.search_text.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\nbackground-color: rgb(95, 95, 95);\ncolor: rgb(255, 255, 255);")
        self.search_text.setText("")
        self.search_text.setObjectName("search_text")
        self.searche = QtWidgets.QPushButton(Dialog)
        self.searche.setGeometry(QtCore.QRect(760, 10, 41, 41))
        self.searche.setStyleSheet('font: 14pt "MS Shell Dlg 2";\nbackground-color: rgb(251,188,4);\ncolor: rgb(0, 0, 0);')
        self.searche.setObjectName("searche")
        self.all_mail = QtWidgets.QPushButton(Dialog)
        self.all_mail.setGeometry(QtCore.QRect(10, 140, 161, 41))
        self.all_mail.setStyleSheet('background-color: rgb(66,133,244);\ncolor: rgb(0,0,0);\nfont: 11pt "MS Shell Dlg 2";')
        self.all_mail.setObjectName("all_mail")
        self.incoming = QtWidgets.QPushButton(Dialog)
        self.incoming.setGeometry(QtCore.QRect(10, 190, 161, 41))
        self.incoming.setStyleSheet('background-color: rgb(66,133,244);\ncolor: rgb(255,255,255);\nfont: 9pt "MS Shell Dlg 2";')
        self.incoming.setObjectName("incoming")
        self.sent = QtWidgets.QPushButton(Dialog)
        self.sent.setGeometry(QtCore.QRect(10, 240, 161, 41))
        self.sent.setStyleSheet('background-color: rgb(66,133,244);\ncolor: rgb(255,255,255);\nfont: 9pt "MS Shell Dlg 2";')
        self.sent.setObjectName("sent")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 560, 160, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dark_theme = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.dark_theme.setStyleSheet('font: 10pt "MS Shell Dlg 2";\ncolor: rgb(255, 255, 255);\nbackground-color: rgb(52,168,83);')
        self.dark_theme.setObjectName("dark_theme")
        self.dark_theme.click()
        self.gridLayout.addWidget(self.dark_theme, 2, 0, 1, 1)
        self.classic_theme = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.classic_theme.setStyleSheet('font: 10pt "MS Shell Dlg 2";\ncolor: rgb(255, 255, 255);\nbackground-color: rgb(52,168,83);')
        self.classic_theme.setObjectName("classic_theme")
        self.gridLayout.addWidget(self.classic_theme, 1, 0, 1, 1)
        self.image = QtWidgets.QLabel(self)
        self.image.move(20, 15)
        self.image.resize(109, 40)
        self.image.setPixmap(QtGui.QPixmap('../files/logo.png'))

        MainW2.retranslateUi(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gmail"))
        self.search_text.setPlaceholderText(_translate("Dialog", 'Поиск по всем цепочкам'))
        self.make_mail.setText(_translate("Dialog", "🖊 Написать"))
        self.update.setText(_translate("Dialog", "⟳"))
        self.forward.setText(_translate("Dialog", ">"))
        self.back.setText(_translate("Dialog", "<"))
        self.label.setText(_translate("Dialog", "1-100"))
        self.searche.setText(_translate("Dialog", "🔍"))
        self.all_mail.setText(_translate("Dialog", "Вся почта"))
        self.incoming.setText(_translate("Dialog", "Входящие"))
        self.sent.setText(_translate("Dialog", "Отправленные"))
        self.dark_theme.setText(_translate("Dialog", "Темная тема"))
        self.classic_theme.setText(_translate("Dialog", "Светлая тема"))
