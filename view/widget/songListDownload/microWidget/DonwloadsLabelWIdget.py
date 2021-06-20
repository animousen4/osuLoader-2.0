from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from view.element.textLabel.types.DownloadsLabel import DownloadsLabel


class DownloadsLabelWidget(QFrame):
    def __init__(self):
        super(DownloadsLabelWidget, self).__init__()

        verticalLayout = QVBoxLayout()

        verticalLayout.setAlignment(Qt.AlignTop)

        verticalLayout.addWidget(DownloadsLabel())

        self.setLayout(verticalLayout)
