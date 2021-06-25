from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout

from view.element.button.types.OsuPathSelectorButton import NextButton, ExitButton


class ActionButtonWidget(QFrame):
    layout = QHBoxLayout
    def __init__(self, bp):
        super(ActionButtonWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignRight)
        self.layout.addWidget(NextButton(bp.onNext))
        self.layout.addWidget(ExitButton(bp.onExit))
    pass