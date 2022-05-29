from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QDockWidget, \
        QScrollArea
from PyQt5.QtGui import QIcon

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
        self.content = QWidget()
        self.toolsDock = parent.findChild(QDockWidget, 'tools_dock')
        self.toolsScroll = parent.findChild(QScrollArea, 'tools_scrollArea')
        self.toolsLayout = parent.findChild(QGridLayout, 'tools_gridLayout')
        self.toolsLayout.setHorizontalSpacing(1)
        self.toolsLayout.setVerticalSpacing(1)
        self.content.setLayout(self.toolsLayout)
        self.toolsDock.setWidget(self.toolsScroll)
        self.toolsDock.setMinimumWidth(200)
        self.toolsScroll.setWidgetResizable(True)
        self.toolsScroll.setWidget(self.content)
        self.loadTools()

    def loadTools(self):
        self.loadPen()

    def loadPen(self):
        self.penButton = QPushButton('', self)
        self.penButton.clicked.connect(self.handlePenButton)
        self.penButton.setIcon(QIcon('./ui/images/pen.jpg'))
        self.penButton.setIconSize(QSize(40, 40))
        self.penButton.setFixedWidth(40)
        self.penButton.setFixedHeight(40)
        self.toolsLayout.addWidget(self.penButton, 0, 0)

    def handlePenButton(self):
        print('clicked')
