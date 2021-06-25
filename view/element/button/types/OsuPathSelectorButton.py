from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

import ResourceNavigator
from view.element.button.ButtonTypes import IconButton, StandardButton


class OpenExplorerButton(IconButton):
    def __init__(self, act):
        super(OpenExplorerButton, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoImportFile))
        self.clicked.connect(lambda state, a = act: act())


class NextButton(StandardButton):
    def __init__(self, act):
        super(NextButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonNext)
        self.clicked.connect(lambda state, a = act: act())


class ExitButton(StandardButton):
    def __init__(self, act):
        super(ExitButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonExit)
        self.clicked.connect(lambda state, a = act: act())