from PyQt5.QtWidgets import QAction, QFileDialog

class MenuBarMgr:
    def __init__(self, parent):
        self.parent = parent

    def connect(self, name, handler):
        action = self.parent.findChild(QAction, name)
        action.triggered.connect(handler)

    def doNew(self):
        print('new')

    def doOpen(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        if dlg.exec_():
           filename = dlg.selectedFiles()
           print(filename)

    def doOpenRecent(self):
        print('open recent')

    def doSave(self):
        print('save')

    def doSaveAs(self):
        print('save as')

    def doImport(self):
        print('import')

    def doExport(self):
        print('export')

    def doQuit(self):
        self.parent.close()

    def doUndo(self):
        print('undo')

    def doRedo(self):
        print('redo')

    def doShowToolbox(self):
        print('show toolbox')

    def doVerinfo(self):
        print('verinfo')
