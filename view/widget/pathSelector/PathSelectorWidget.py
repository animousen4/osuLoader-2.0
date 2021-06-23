from PyQt5.QtWidgets import QWidget, QHBoxLayout

from view.element.button.types.OsuPathSelectorButton import OpenExplorerButton
from view.element.inputLabel.types.InputLabelSelectPath import InputLabelSelectPath


class PathSelectorWidget(QWidget):
    inputLabelSelectPath = InputLabelSelectPath
    buttonOpenExplorer = OpenExplorerButton

    def __init__(self):
        super(PathSelectorWidget, self).__init__()

        horizontalLayout = QHBoxLayout()

        self.inputLabelSelectPath = InputLabelSelectPath()

        self.buttonOpenExplorer = OpenExplorerButton()

        horizontalLayout.addWidget(self.inputLabelSelectPath)

        horizontalLayout.addWidget(self.buttonOpenExplorer)

        self.setLayout(horizontalLayout)
