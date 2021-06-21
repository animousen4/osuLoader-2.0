from PyQt5.QtGui import QIcon

import ResourceNavigator
from view.element.button.ButtonTypes import IconButton


class ActionButton(IconButton):
    def __init__(self):
        super(ActionButton, self).__init__()


class ActionButtonDeleteFile(ActionButton):
    def __init__(self):
        super(ActionButtonDeleteFile, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoDeleteFile))


class ActionButtonCancelDownload(ActionButton):
    def __init__(self):
        super(ActionButtonCancelDownload, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoCancelDownload))


class ActionButtonImport(ActionButton):
    def __init__(self):
        super(ActionButtonImport, self).__init__()
        self.setIcon(QIcon(ResourceNavigator.MaterialNavigator.icoImportFile))