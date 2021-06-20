from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout

from view.element.button.ImportDelAllButton import ImportAllButton, DeleteAllButton


class ImportDelAllButtonWidget(QFrame):
    buttonImportAll = ImportAllButton
    buttonDeleteAll = DeleteAllButton

    def __init__(self):
        super(ImportDelAllButtonWidget, self).__init__()

        horizontalLayout = QHBoxLayout()

        horizontalLayout.setAlignment(Qt.AlignBottom)

        self.buttonImportAll = ImportAllButton()

        self.buttonDeleteAll = DeleteAllButton()

        horizontalLayout.addWidget(self.buttonImportAll)

        horizontalLayout.addWidget(self.buttonDeleteAll)

        self.setLayout(horizontalLayout)

