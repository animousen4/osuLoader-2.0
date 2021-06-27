from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QWidget

from view.element.button.types.OsuPathSelectorButton import NextButton, ExitButton


class ActionButtonWidget(QFrame):
    layout = QHBoxLayout
    exitButton = ExitButton
    nextButton = NextButton

    def __init__(self, bp):
        super(ActionButtonWidget, self).__init__()
        self.layout = QHBoxLayout()
        #self.layout.setAlignment(Qt.AlignRight)
        self.exitButton = ExitButton(bp.onExit)
        self.nextButton = NextButton(bp.onNext)

        layoutButtonExit = QHBoxLayout()
        layoutButtonExit.setAlignment(Qt.AlignLeft)
        widgetButtonExit = QWidget()
        layoutButtonExit.addWidget(self.exitButton)
        widgetButtonExit.setLayout(layoutButtonExit)

        layoutButtonNext = QHBoxLayout()
        layoutButtonNext.setAlignment(Qt.AlignRight)
        widgetButtonNext = QWidget()
        layoutButtonNext.addWidget(self.nextButton)
        widgetButtonNext.setLayout(layoutButtonNext)

        self.layout.addWidget(widgetButtonExit)
        self.layout.addWidget(widgetButtonNext)
        self.setLayout(self.layout)
    pass