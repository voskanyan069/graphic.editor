from PyQt5.QtWidgets import QSlider, QSizePolicy
from PyQt5.QtCore import Qt

class ToolsSlider(QSlider):
    def __init__(self, handler, minVal=0,maxVal=100, orientation=Qt.Horizontal):
        super(ToolsSlider, self).__init__()
        po = QSizePolicy()
        self.setMinimum(minVal)
        self.setMaximum(maxVal)
        self.setOrientation(orientation)
        self.valueChanged[int].connect(handler)
