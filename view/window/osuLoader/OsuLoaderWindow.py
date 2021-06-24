from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import ResourceNavigator
from back.AppBackend import AppBackendInit
from back.css.style import cssLoader
from view.window.osuLoader.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout


class OsuLoaderWindow(QWidget):
    osuLoaderWindowLayout = OsuLoaderWindowLayout
    appBackend = AppBackendInit

    def __init__(self):
        super(OsuLoaderWindow, self).__init__()

        print("Open OsuLoaderWindow")

        self.initUI()

    def initUI(self):
        print("Init UI...")

        self.setWindowTitle(ResourceNavigator.Variables.Strings.osuLoaderWindowName)

        self.initFonts()

        self.initStyles()

        self.osuLoaderWindowLayout = OsuLoaderWindowLayout()

        self.appBackend = AppBackendInit(self.osuLoaderWindowLayout)

        self.setLayout(self.osuLoaderWindowLayout)

        self.setMinimumSize(1280, 720)

        self.appBackend.postInit()

        self.show()

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

