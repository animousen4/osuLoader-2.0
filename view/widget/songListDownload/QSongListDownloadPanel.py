from PyQt5.QtWidgets import QFrame, QVBoxLayout

from view.widget.songListDownload.microWidget.ImportDelAllButtonWidget import ImportDelAllButtonWidget


class QSongListDownloadPanel(QFrame):

    importDelButtons = ImportDelAllButtonWidget

    def __init__(self):
        super(QSongListDownloadPanel, self).__init__()

        verticalLayout = QVBoxLayout()

        self.importDelButtons = ImportDelAllButtonWidget()

        verticalLayout.addWidget(self.importDelButtons)

        self.setLayout(verticalLayout)
