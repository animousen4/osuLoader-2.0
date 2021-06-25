from PyQt5.QtGui import QIcon

import ResourceNavigator
from view.element.button.ButtonTypes import IconButton, MediumButton


class OpenExplorerButton(IconButton):
    def __init__(self, act):
        super(OpenExplorerButton, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoImportFile))
        self.clicked.connect(lambda state, a = act: act())


class NextButton(MediumButton):
    def __init__(self, f):
        super(NextButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonNext)
        self.clicked.connect(f)


class ExitButton(MediumButton):
    def __init__(self, f):
        super(ExitButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonExit)
        self.clicked.connect(f)