from flowlayout import FlowLayout
from toolsbutton import ToolsButton
from toolsslider import ToolsSlider
from configmgr import ConfigMgr

from PyQt5.QtWidgets import QWidget, QPushButton, QDockWidget, \
        QScrollArea, QVBoxLayout, QHBoxLayout, QSpacerItem, QLabel, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

# TODO: Add tools listed below
# fill (pen color)
# text
# crop
# import/export

class Toolbox(QWidget):
    def __init__(self, parent):
        super(Toolbox, self).__init__(parent)
        self.btnSize = 35
        self.configMgr = ConfigMgr()
        self.content = QWidget()
        self.toolsButtonsLayout = FlowLayout()
        self.toolsLayout = QVBoxLayout()
        self.toolsLayout.setAlignment(Qt.AlignTop)
        self.toolsLayout.setSpacing(0)
        self.toolsLayout.addLayout(self.toolsButtonsLayout)
        self.toolsDock = parent.findChild(QDockWidget, 'tools_dock')
        self.toolsScroll = parent.findChild(QScrollArea, 'tools_scrollArea')
        self.content.setLayout(self.toolsLayout)
        self.toolsDock.setWidget(self.toolsScroll)
        self.toolsDock.setMinimumWidth(240)
        self.toolsScroll.setWidgetResizable(True)
        self.toolsScroll.setWidget(self.content)
        self.toolsDock.setStyleSheet('padding: 5px')
        self.loadTools()

    def loadTools(self):
        self.loadPen()
        self.loadEraser()
        self.loadFill()
        self.loadText()
        self.loadCrop()
        self.loadPenSize()
        self.loadColorPicker()

    def loadPen(self):
        self.penButton = ToolsButton('./ui/images/pen.svg', self.btnSize, \
                self.btnSize-15, self.handlePenButton)
        self.toolsButtonsLayout.addWidget(self.penButton)

    def loadEraser(self):
        self.eraserButton = ToolsButton('./ui/images/eraser.svg', self.btnSize,\
                self.btnSize-10, self.handlePenButton)
        self.toolsButtonsLayout.addWidget(self.eraserButton)

    def loadFill(self):
        self.fillButton = ToolsButton('./ui/images/fill.svg', self.btnSize, \
                self.btnSize-10, self.onFillButtonClicked)
        self.toolsButtonsLayout.addWidget(self.fillButton)

    def loadText(self):
        self.textButton = ToolsButton('./ui/images/text.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsButtonsLayout.addWidget(self.textButton)

    def loadCrop(self):
        self.cropButton = ToolsButton('./ui/images/crop.svg', self.btnSize, \
                self.btnSize-10, self.handlePenButton)
        self.toolsButtonsLayout.addWidget(self.cropButton)

    def loadPenSize(self):
        verticalSpacer = QSpacerItem(0, 50)
        layout = QHBoxLayout()
        self.penSizeLabel = QLabel(f'Pen size {self.configMgr.getPenSize()}')
        self.penSizeSlider = ToolsSlider(self.onPenSizeChanged, 1, 100)
        layout.addWidget(self.penSizeLabel)
        layout.addWidget(self.penSizeSlider)
        self.toolsLayout.addItem(verticalSpacer)
        self.toolsLayout.addLayout(layout)

    def loadColorPicker(self):
        layout = QHBoxLayout()
        label = QLabel('Selected color: ')
        self.selectedColor = QPushButton('#000000')
        self.selectedColor.clicked.connect(self.onColorPickerClicked)
        self.selectedColor.setFixedSize(80, 30)
        layout.addWidget(label)
        layout.addWidget(self.selectedColor)
        self.toolsLayout.addLayout(layout)

    def handlePenButton(self):
        print('clicked')

    def onFillButtonClicked(self):
        # TODO
        self.configMgr.setFillColor(self.configMgr.getPenColor())

    def onPenSizeChanged(self, newValue):
        self.configMgr.setPenSize(newValue)
        self.penSizeLabel.setText(f'Pen size {newValue}')

    def onColorPickerClicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selectedColor.setText(color.name())
            self.configMgr.setPenColor(color)
        else:
            self.selectedColor.setText(self.configMgr.getPenColor().name())
