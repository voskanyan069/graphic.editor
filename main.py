#!./venv/bin/python3

import sys

from modules import MenuBarMgr, Toolbox, Canvas

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from qt_material import apply_stylesheet

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.setWindowTitle("Graphic Editor")
        self.createComponents()
        self.connectMenuAction()
        self.show()

    def createComponents(self):
        self.menuMgr = MenuBarMgr(self)
        self.toolbox = Toolbox(self)
        self.canvas = Canvas(self)

    def connectMenuAction(self):
        self.menuMgr.connect('actionNew', self.menuMgr.doNew)
        self.menuMgr.connect('actionOpen', self.menuMgr.doOpen)
        self.menuMgr.connect('actionOpen_Recent', self.menuMgr.doOpenRecent)
        self.menuMgr.connect('actionSave', self.menuMgr.doSave)
        self.menuMgr.connect('actionSave_as', self.menuMgr.doSaveAs)
        self.menuMgr.connect('actionImport', self.menuMgr.doImport)
        self.menuMgr.connect('actionExport', self.menuMgr.doExport)
        self.menuMgr.connect('actionQuit', self.menuMgr.doQuit)
        self.menuMgr.connect('actionUndo', self.menuMgr.doUndo)
        self.menuMgr.connect('actionRedo', self.menuMgr.doRedo)
        self.menuMgr.connect('actionShow_Toolbox', self.menuMgr.doShowToolbox)
        self.menuMgr.connect('actionVerinfo',self.menuMgr.doVerinfo)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    apply_stylesheet(app, theme='dark_amber.xml')
    app.exec_()
