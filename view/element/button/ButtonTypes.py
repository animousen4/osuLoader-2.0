from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton


class IconButton(QPushButton):
    def __init__(self):
        super(IconButton, self).__init__()
        self.setIconSize(QSize(15, 15))
        self.setFixedSize(QSize(18, 18))
    pass


class StandardButton(QPushButton):
    def __init__(self):
        super(StandardButton, self).__init__()
        self.setMinimumSize(60, 20)
    pass


class LevelButton(QPushButton):
    def __init__(self):
        super(LevelButton, self).__init__()

    pass
