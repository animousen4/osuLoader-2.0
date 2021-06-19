from PyQt5.QtWidgets import QWidget

import ResourceNavigator


class OsuLoaderWindow(QWidget):
    def __init__(self):
        super(OsuLoaderWindow, self).__init__()
        self.initBack()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(ResourceNavigator.Variables.Strings.windowName)

        self.show()

    def initBack(self):
        pass
