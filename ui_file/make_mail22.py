from PyQt5 import QtCore, QtWidgets

class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.combo = ComboBox(self)
        self.combo.popupAboutToBeShown.connect(self.populateConbo)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.combo)

    def populateConbo(self):
        if not self.combo.count():
            self.combo.addItems('One Two Three Four'.split())

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())