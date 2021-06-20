from PyQt5.QtWidgets import QLabel


class LargeLabel(QLabel):
    pass


class SmallLabel(QLabel):
    def __init__(self):
        super(SmallLabel, self).__init__()
       