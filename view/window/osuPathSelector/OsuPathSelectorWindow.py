from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import ResourceNavigator
from back.css.style import cssLoader
from back.osuSelector.AppBackend import AppBackendInit
from view.window.osuPathSelector.layout.OsuPathSelectorWindowLayout import OsuPathSelectorWindowLayout


class OsuPathSelectorWindow(QWidget):
    def __init__(self):
        super(OsuPathSelectorWindow, self).__init__()

        print("Open OsuPathSelectorWindow")

        self.initStyles()

        self.initFonts()

        self.initUI()


    def initUI(self):

        self.setWindowTitle(ResourceNavigator.Variables.Strings.osuPathSelectorWindowName)

        self.setMinimumSize(640, 360)

        layout = OsuPathSelectorWindowLayout()

        appBackend = AppBackendInit(layout)

        self.setLayout(layout)

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