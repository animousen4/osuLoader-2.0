from PyQt5.QtWidgets import QHBoxLayout, QFrame

from view.element.button.types.OsuPathSelectorButton import OpenExplorerButton
from view.element.inputLabel.types.InputLabelSelectPath import InputLabelSelectPath


class PathSelectorWidget(QFrame):
    inputLabelSelectPath = InputLabelSelectPath
    buttonOpenExplorer = OpenExplorerButton

    def __init__(self, bp):
        super(PathSelectorWidget, self).__init__()

        horizontalLayout = QHBoxLayout()

        self.inputLabelSelectPath = InputLabelSelectPath(bp.onEdit)

        self.buttonOpenExplorer = OpenExplorerButton(bp.onOpenExplorer)

        horizontalLayout.addWidget(self.inputLabelSelectPath)

        horizontalLayout.addWidget(self.buttonOpenExplorer)

        self.setLayout(horizontalLayout)
