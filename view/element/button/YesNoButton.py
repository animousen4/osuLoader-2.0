from PyQt5.QtWidgets import QPushButton


class YesNoButton(QPushButton):
    pass

class YesButton(YesNoButton):
    def __init__(self):
        super(YesButton, self).__init__()
        self.setText("Yes")

