from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import ResourceNavigator
from back.FileManager import LoaderLevelManager
from back.css.style import cssLoader


class OsuLoaderWindow(QWidget):
    def __init__(self):
        super(OsuLoaderWindow, self).__init__()
        self.initBack()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(ResourceNavigator.Variables.Strings.windowName)

        self.initFonts()

        self.initStyles()

        fileManager = LoaderLevelManager()

        fileManager.loadLoaderLevels()

        self.show()

    def initBack(self):
        pass

    def initStyles(self):
        print("Init styles...")
        loader = cssLoader()
        css = loader.getStyleSheet()
        self.setStyleSheet(css)

    def initFonts(self):
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoRegular)
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoThin)
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoBold)
