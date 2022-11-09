# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(983, 613)
        self.make_mail = QtWidgets.QPushButton(Dialog)
        self.make_mail.setGeometry(QtCore.QRect(10, 80, 111, 41))
        self.make_mail.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.make_mail.setObjectName("make_mail")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(130, 80, 41, 41))
        self.update.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.update.setObjectName("update")
        self.forwsrd = QtWidgets.QPushButton(Dialog)
        self.forwsrd.setGeometry(QtCore.QRect(950, 20, 21, 23))
        self.forwsrd.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.forwsrd.setObjectName("forwsrd")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(920, 20, 21, 23))
        self.back.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(840, 20, 61, 20))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.search_text = QtWidgets.QLineEdit(Dialog)
        self.search_text.setGeometry(QtCore.QRect(182, 10, 571, 41))
        self.search_text.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(226, 226, 226);")
        self.search_text.setText("")
        self.search_text.setObjectName("search_text")
        self.searche = QtWidgets.QPushButton(Dialog)
        self.searche.setGeometry(QtCore.QRect(760, 10, 41, 41))
        self.searche.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.searche.setObjectName("searche")
        self.all_mail = QtWidgets.QPushButton(Dialog)
        self.all_mail.setGeometry(QtCore.QRect(10, 140, 161, 41))
        self.all_mail.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.all_mail.setObjectName("all_mail")
        self.incoming = QtWidgets.QPushButton(Dialog)
        self.incoming.setGeometry(QtCore.QRect(10, 190, 161, 41))
        self.incoming.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.incoming.setObjectName("incoming")
        self.sent = QtWidgets.QPushButton(Dialog)
        self.sent.setGeometry(QtCore.QRect(10, 240, 161, 41))
        self.sent.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.sent.setObjectName("sent")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 560, 160, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dark_theme = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.dark_theme.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dark_theme.setObjectName("dark_theme")
        self.gridLayout.addWidget(self.dark_theme, 2, 0, 1, 1)
        self.classic_theme = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.classic_theme.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.classic_theme.setObjectName("classic_theme")
        self.gridLayout.addWidget(self.classic_theme, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(180, 80, 801, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.make_mail.setText(_translate("Dialog", "🖊 Написать"))
        self.update.setText(_translate("Dialog", "🔄"))
        self.forwsrd.setText(_translate("Dialog", ">"))
        self.back.setText(_translate("Dialog", "<"))
        self.label.setText(_translate("Dialog", "1-100"))
        self.searche.setText(_translate("Dialog", "🔍"))
        self.all_mail.setText(_translate("Dialog", "Вся почта"))
        self.incoming.setText(_translate("Dialog", "Входящие"))
        self.sent.setText(_translate("Dialog", "Отправленные"))
        self.dark_theme.setText(_translate("Dialog", "Темная тема"))
        self.classic_theme.setText(_translate("Dialog", "Свтелая тема"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "От"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Кому"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Тема"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Дата"))
