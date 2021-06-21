from PyQt5.QtWidgets import QFrame, QVBoxLayout

from view.element.textLabel.types.DownloadsLabel import DownloadsLabel
from view.widget.songListDownload.microWidget.DonwloadsLabelWidget import DownloadsLabelWidget
from view.widget.songListDownload.microWidget.ImportDelAllButtonWidget import ImportDelAllButtonWidget


class QSongListDownloadPanel(QFrame):

    importDelButtons = ImportDelAllButtonWidget

    def __init__(self):
        super(QSongListDownloadPanel, self).__init__()

        verticalLayout = QVBoxLayout()

        self.importDelButtons = ImportDelAllButtonWidget()

        verticalLayout.addWidget(DownloadsLabelWidget())

        verticalLayout.addWidget(self.importDelButtons)

        self.setLayout(verticalLayout)

