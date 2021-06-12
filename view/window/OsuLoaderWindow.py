from PyQt5.QtWidgets import QWidget


class OsuLoaderWindow(QWidget):
    def __init__(self):
        super(OsuLoaderWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle()
