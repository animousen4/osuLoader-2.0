from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QProgressBar

from view.element.button.YesNoButton import YesButton
from view.widget.browser.QBrowserWidget import QBrowserWidget
from view.widget.songListDownload.QSongListDownloadPanel import QSongListDownloadPanel


class OsuLoaderWindowLayout(QHBoxLayout):
    browserWidget = QBrowserWidget
    songPanel = QSongListDownloadPanel
    def __init__(self):
        super(OsuLoaderWindowLayout, self).__init__()

        self.setContentsMargins(0, 0, 0, 0)

        self.browserWidget = QBrowserWidget()

        self.songPanel = QSongListDownloadPanel()

        self.initWidgets()

    def initWidgets(self):
        self.addWidget(self.browserWidget, 4)
        self.addWidget(self.songPanel, 1)

