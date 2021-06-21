from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import ResourceNavigator
from back.AppBackend import AppBackend
from back.css.style import cssLoader
from view.window.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout


class OsuLoaderWindow(QWidget):
    osuLoaderWindowLayout = OsuLoaderWindowLayout
    appBackend = AppBackend

    def __init__(self):
        super(OsuLoaderWindow, self).__init__()
        self.initUI()

    def initUI(self):
        print("Init UI...")

        self.setWindowTitle(ResourceNavigator.Variables.Strings.windowName)

        self.initFonts()

        self.initStyles()

        self.osuLoaderWindowLayout = OsuLoaderWindowLayout()

        self.setLayout(self.osuLoaderWindowLayout)

        self.setFixedSize(1280, 720)

        self.show()

        self.appBackend = AppBackend(self.osuLoaderWindowLayout)


    def initStyles(self):
        print("Init styles...")
        loader = cssLoader()
        css = loader.getStyleSheet()
        self.setStyleSheet(css)

    def initFonts(self):
        print("Init fonts...")
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoRegular)
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoThin)
        QtGui.QFontDatabase.addApplicationFont(ResourceNavigator.FontsNavigator.fontExoBold)

