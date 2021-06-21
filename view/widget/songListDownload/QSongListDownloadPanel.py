from PyQt5.QtWidgets import QFrame, QVBoxLayout

from view.element.textLabel.types.DownloadsLabel import DownloadsLabel
from view.widget.songListDownload.microWidget.DownloadsLabelWidget import DownloadsLabelWidget
from view.widget.songListDownload.microWidget.ImportDelAllButtonWidget import ImportDelAllButtonWidget
from view.widget.songListDownload.microWidget.SongDownloadListWidget import SongDownloadListWidget


class QSongListDownloadPanel(QFrame):

    songDownloadList = SongDownloadListWidget

    def __init__(self):
        super(QSongListDownloadPanel, self).__init__()

        verticalLayout = QVBoxLayout()

        self.importDelButtons = ImportDelAllButtonWidget()

        self.songDownloadList = SongDownloadListWidget()

        verticalLayout.addWidget(DownloadsLabelWidget())

        verticalLayout.addWidget(self.songDownloadList)
        #verticalLayout.addWidget(self.importDelButtons)

        self.setLayout(verticalLayout)

