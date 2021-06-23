from PyQt5.QtGui import QIcon

import ResourceNavigator
from view.element.button.ButtonTypes import IconButton


class OpenExplorerButton(IconButton):
    def __init__(self):
        super(OpenExplorerButton, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoImportFile))
