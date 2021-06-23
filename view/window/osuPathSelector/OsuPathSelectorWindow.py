from PyQt5.QtWidgets import QWidget

import ResourceNavigator
from view.window.osuPathSelector.layout.OsuPathSelectorWindowLayout import OsuPathSelectorWindowLayout


class OsuPathSelectorWindow(QWidget):
    def __init__(self):
        super(OsuPathSelectorWindow, self).__init__()

        print("Open OsuPathSelectorWindow")

        self.initUI()

    def initUI(self):

        self.setWindowTitle(ResourceNavigator.Variables.Strings.osuPathSelectorWindowName)

        self.setMinimumSize(640, 360)

        layout = OsuPathSelectorWindowLayout()

        self.setLayout(layout)

        self.show()
