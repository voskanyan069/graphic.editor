from configmgr import ConfigMgr

from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QLabel

class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.configMgr = ConfigMgr()
        parent.setCentralWidget(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), self.configMgr.getFillColor())
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(200, 200)
        self.setMinimumSize(200, 200)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(self.configMgr.getPenColor())
        self.painter.setPen(self.pen)
        self.painter.fillRect(0, 0, 200, 200, self.configMgr.getFillColor())
        self.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())
            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.pen = QPen(self.configMgr.getPenColor())
        self.pen.setWidth(self.configMgr.getPenSize())
        self.painter.setPen(self.pen)
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def updateSize(self, width, height):
        pm = QPixmap(width, height)
        pm.fill(self.configMgr.getFillColor())
        old = self.myPixmap
        self.myPixmap = pm
        self.pen = QPen(self.configMgr.getPenColor())
        self.painter = QPainter(pm)
        self.painter.drawPixmap(0, 0, old)
        self.setPixmap(pm)

    def resizeEvent(self, event):
        if event.oldSize().width() > 0:
            self.updateSize(event.size().width(), event.size().height())
