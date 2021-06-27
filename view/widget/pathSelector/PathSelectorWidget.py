from PyQt5.QtWidgets import QHBoxLayout, QFrame, QVBoxLayout, QWidget

from view.element.button.types.OsuPathSelectorButton import OpenExplorerButton
from view.element.inputLabel.types.InputLabelSelectPath import InputLabelSelectPath
from view.element.textLabel.types.HintLabel import HintLabel


class PathSelectorWidget(QFrame):
    inputLabelSelectPath: InputLabelSelectPath
    buttonOpenExplorer: OpenExplorerButton
    hintLabel: HintLabel

    def __init__(self, bp):
        super(PathSelectorWidget, self).__init__()

        horizontalLayout = QHBoxLayout()

        verticalLayout = QVBoxLayout()
        verticalLayoutWidget = QWidget()
        verticalLayoutWidget.setLayout(verticalLayout)

        self.inputLabelSelectPath = InputLabelSelectPath(bp.onEdit)

        self.hintLabel = HintLabel()

        self.buttonOpenExplorer = OpenExplorerButton(bp.onOpenExplorer)

        verticalLayout.addWidget(self.inputLabelSelectPath)
        verticalLayout.addWidget(self.hintLabel)

        horizontalLayout.addWidget(verticalLayoutWidget)

        horizontalLayout.addWidget(self.buttonOpenExplorer)

        self.setLayout(horizontalLayout)
