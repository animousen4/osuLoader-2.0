from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem, QWebEngineProfile

import ResourceNavigator
from back.fileManager.FileManager import LoaderLevelManager
from back.objects.song.Song import SongShortInfo
from view.widget.browser.QBrowserWidget import QBrowserWidget
from view.widget.songListDownload.microWidget.SongDownloadListWidget import MapWidget
from view.window.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout


class AppBackendInit:
    def __init__(self, layout=OsuLoaderWindowLayout):
        OnStart(layout)
        BrowserBackend(layout)


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


class BrowserBackend(AppBackendAction):
    def setup(self):
        self.loadBeatMapPage()
        self.setupBindings()
        pass

    def loadBeatMapPage(self):
        self.windowLoaderLayout.browserWidget.load(QUrl(ResourceNavigator.Local.Url.beatMapUrl))

    def setupBindings(self):
        self.windowLoaderLayout.browserWidget.downloadSignal.connect(self.onDownloadRequest)
        #self.windowLoaderLayout.browserWidget.page().profile().downloadRequested.connect(self.onDownloadRequest)
        pass

    def onDownloadRequest(self, d=QWebEngineDownloadItem):
        print("Download Requested")
        d.cancel()
        pass
