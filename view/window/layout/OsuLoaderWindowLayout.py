from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QProgressBar

from view.element.button.YesNoButton import YesButton
from view.widget.browser.QBrowserWidget import QBrowserWidget
from view.widget.songListDownload.QSongListDownload import QSongListDownload


class OsuLoaderWindowLayout(QHBoxLayout):
    def __init__(self):
        super(OsuLoaderWindowLayout, self).__init__()

        self.setContentsMargins(0, 0, 0, 0)

        self.initWidgets()

    def initWidgets(self):
        self.addWidget(QBrowserWidget(), 4)
        self.addWidget(QSongListDownload(), 1)

