from PyQt5.QtGui import QColor, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QLabel

class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        parent.setCentralWidget(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#fff'))
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(200,200)
        self.setMinimumSize(200,200)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(QColor('#000'))
        self.painter.setPen(self.pen)
        self.painter.fillRect(0,0,200,200, QColor('#fff'))
        self.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())
            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def updateSize(self, width, height):
        pm = QPixmap(width, height)
        pm.fill(QColor('#fff'))
        old = self.myPixmap
        self.myPixmap = pm
        self.pen = QPen(QColor('#000'))
        self.painter = QPainter(pm)
        self.painter.drawPixmap(0,0,old)
        self.setPixmap(pm)

    def resizeEvent(self, event):
        if event.oldSize().width() > 0:
            self.updateSize(event.size().width(), event.size().height())
