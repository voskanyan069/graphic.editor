from PyQt5.QtGui import QColor

class ConfigMgr(object):
    instance = None

    class __ConfigMgr:
        def __init__(self):
            self.__penSize = None
            self.__penColor = None
            self.__bgColor = None

        def getPenSize(self):
            if self.__penSize == None:
                return 1
            return self.__penSize

        def setPenSize(self, size):
            self.__penSize = size

        def getPenColor(self):
            if self.__penColor == None:
                return QColor('#000')
            return self.__penColor

        def setPenColor(self, color):
            self.__penColor = color

        def getFillColor(self):
            if self.__bgColor == None:
                return QColor('#fff')
            return self.__bgColor

        def setFillColor(self, color):
            self.__bgColor = color

    def __new__(cls):
        if not ConfigMgr.instance:
            ConfigMgr.instance = ConfigMgr.__ConfigMgr()
        return ConfigMgr.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
