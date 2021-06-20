from PyQt5.QtWidgets import QFrame, QHBoxLayout

from view.element.button.ImportDelAllButton import ImportAllButton, DeleteAllButton


class ImportDelAllButtonWidget(QFrame):
    buttonImportAll = None
    buttonDeleteAll = None

    def __init__(self):
        super(ImportDelAllButtonWidget, self).__init__()

        horizontalLayout = QHBoxLayout()

        self.buttonImportAll = ImportAllButton()

        self.buttonDeleteAll = DeleteAllButton()

        horizontalLayout.addWidget(self.buttonImportAll)

        horizontalLayout.addWidget(self.buttonDeleteAll)

        self.setLayout(horizontalLayout)
