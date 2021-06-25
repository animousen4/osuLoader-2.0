from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from view.element.textLabel.types.DownloadsLabel import DownloadsLabel
from view.widget.songListDownload.microWidget.DownloadsLabelWidget import DownloadsLabelWidget
from view.widget.songListDownload.microWidget.ImportDelAllButtonWidget import ImportDelAllButtonWidget
from view.widget.songListDownload.microWidget.SongDownloadListWidget import SongDownloadListWidget, \
    ActionButtonPanelWidget


class QSongListDownloadPanel(QFrame):

    importDelAllButtons = ImportDelAllButtonWidget

    songDownloadList = SongDownloadListWidget

    def __init__(self, bp):
        super(QSongListDownloadPanel, self).__init__()

        verticalLayout = QVBoxLayout()

        #verticalLayout.setAlignment(Qt.AlignTop)

        self.importDelAllButtons = ImportDelAllButtonWidget(bp)

        self.songDownloadList = SongDownloadListWidget()

        verticalLayout.addWidget(DownloadsLabelWidget(), 1)

        verticalLayout.addWidget(self.songDownloadList, 10)

        verticalLayout.addWidget(self.importDelAllButtons, 1)
        #verticalLayout.addWidget(self.importDelButtons)

        self.setLayout(verticalLayout)

