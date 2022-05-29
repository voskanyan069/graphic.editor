#!./venv/bin/python3

import sys

from modules import Toolbox, Canvas

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from qt_material import apply_stylesheet

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.setWindowTitle("Graphic Editor")
        self.createComponents()
        self.show()

    def createComponents(self):
        self.toolbox = Toolbox(self)
        self.canvas = Canvas(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    apply_stylesheet(app, theme='dark_amber.xml')
    app.exec_()
