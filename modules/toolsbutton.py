from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class ToolsButton(QPushButton):
    def __init__(self, imageUri, btnSize, imgSize, handler):
        super(ToolsButton, self).__init__()
        self.clicked.connect(handler)
        self.setIcon(QIcon(imageUri))
        self.setIconSize(QSize(imgSize, imgSize))
        self.setFixedSize(btnSize, btnSize)
