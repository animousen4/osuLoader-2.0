from PyQt5.QtCore import QUrl, pyqtSignal, QObject
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem, QWebEngineProfile

import ResourceNavigator
from back.fileManager.FileManager import LoaderLevelManager
from back.objects.song.Song import SongShortInfo
from view.widget.browser.QBrowserWidget import QBrowserWidget
from view.widget.songListDownload.microWidget.SongDownloadListWidget import MapWidget
from view.window.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout


class AppBackendInit:
    layout = OsuLoaderWindowLayout

    def __init__(self, layout=OsuLoaderWindowLayout):
        self.layout = layout
        self.preInit()

    def preInit(self):
        BrowserBackend(self.layout)

    def postInit(self):
        OnStart(self.layout)



class AppBackendAction:
    windowLoaderLayout = OsuLoaderWindowLayout

    def __init__(self, layout=OsuLoaderWindowLayout):
        self.windowLoaderLayout = layout
        self.setup()

    def setup(self):
        pass


class OnStart(AppBackendAction):

    def setup(self):
        self.openDownloadSongs()
        self.loadBeatMapPage()

    def openDownloadSongs(self):
        fileManager = LoaderLevelManager()
        songs = fileManager.loadLoaderLevels()
        for song in songs:
            self.addDownloaderSongToView(song)

    def addDownloaderSongToView(self, song=SongShortInfo):
        mapWidget = MapWidget()
        mapWidget.commonSongData.setSongData(song)
        mapWidget.mapActionButtons.setStatusDownloadFinished()
        self.windowLoaderLayout.songPanel.songDownloadList.mapList.addSong(mapWidget)

    def loadBeatMapPage(self):
        self.windowLoaderLayout.browserWidget.load(QUrl(ResourceNavigator.Local.Url.beatMapUrl))


class BrowserBackend(AppBackendAction):
    def setup(self):
        browser = QBrowserWidget(self.onDownloadRequest)
        self.windowLoaderLayout.browserWidget = browser
        self.windowLoaderLayout.initWidgets()
        pass

    def onDownloadRequest(self, d=QWebEngineDownloadItem):

        print("Download Requested {}".format(d.suggestedFileName()))
        d.cancel()
        pass
