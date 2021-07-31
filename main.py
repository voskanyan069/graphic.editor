#!./venv/bin/python3

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, \
    QDockWidget, QScrollArea, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from qt_material import apply_stylesheet

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.setWindowTitle("Graphic Editor")
        # self.showMaximized()
        self.load_components()
        self.show()

    def load_components(self):
        self.load_tools()
        self.load_canvas()

    def load_tools(self):
        content = QWidget()
        self.tools_dock = self.findChild(QDockWidget, 'tools_dock')
        tools_scroll = self.findChild(QScrollArea, 'tools_scrollArea')

        self.tools_dock.setWidget(tools_scroll)
        self.tools_dock.setMinimumWidth(200)
        tools_scroll.setWidget(content)
        tools_scroll.setWidgetResizable(True)

    def load_canvas(self):
        self.label = QLabel()
        self.canvas = QPixmap(400,300)
        self.canvas.fill(QColor(255,255,255))
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    apply_stylesheet(app, theme='dark_amber.xml')
    app.exec_()
