from PyQt5.QtGui import QIcon

import ResourceNavigator
from view.element.button.ButtonTypes import IconButton


class OpenExplorerButton(IconButton):
    def __init__(self, act):
        super(OpenExplorerButton, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoImportFile))
        self.clicked.connect(lambda state, a = act: act())
