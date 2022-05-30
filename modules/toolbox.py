from flowlayout import FlowLayout
from toolsbutton import ToolsButton

from PyQt5.QtWidgets import QWidget, QPushButton, QDockWidget, \
        QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

# TODO: Add tools listed below
# pen
#    size
#    color
# fill (pen color)
# text
# crop
# import/export

class Toolbox(QWidget):
    def __init__(self, parent):
        super(Toolbox, self).__init__(parent)
        self.btnSize = 35
        self.content = QWidget()
        self.toolsLayout = FlowLayout()
        self.toolsDock = parent.findChild(QDockWidget, 'tools_dock')
        self.toolsScroll = parent.findChild(QScrollArea, 'tools_scrollArea')
        self.content.setLayout(self.toolsLayout)
        self.toolsDock.setWidget(self.toolsScroll)
        self.toolsDock.setMinimumWidth(200)
        self.toolsScroll.setWidgetResizable(True)
        self.toolsScroll.setWidget(self.content)
        self.loadTools()

    def loadTools(self):
        self.loadPen()
        self.loadEraser()
        self.loadFill()
        self.loadText()
        self.loadCrop()

    def loadPen(self):
        self.penButton = ToolsButton('./ui/images/pen.svg', self.btnSize, \
                self.btnSize-15, self.handlePenButton)
        self.toolsLayout.addWidget(self.penButton)

    def loadEraser(self):
        self.eraserButton = ToolsButton('./ui/images/eraser.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsLayout.addWidget(self.eraserButton)

    def loadFill(self):
        self.fillButton = ToolsButton('./ui/images/fill.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsLayout.addWidget(self.fillButton)

    def loadText(self):
        self.textButton = ToolsButton('./ui/images/text.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsLayout.addWidget(self.textButton)

    def loadCrop(self):
        self.cropButton = ToolsButton('./ui/images/crop.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsLayout.addWidget(self.cropButton)

    def handlePenButton(self):
        print('clicked')
