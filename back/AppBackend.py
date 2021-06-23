from PyQt5.QtCore import QUrl, pyqtSignal, QObject
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem, QWebEngineProfile

import ResourceNavigator
from back.fileManager import FileManager
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
        songListBackend = SongListBackend(self.windowLoaderLayout)
        for song in songs:
            songListBackend.addDownloaderSongToView(song)

    def loadBeatMapPage(self):
        self.windowLoaderLayout.browserWidget.load(QUrl(ResourceNavigator.Local.Url.beatMapUrl))


class SongListBackend(AppBackendAction):
    def addDownloaderSongToView(self, song=SongShortInfo):
        mapWidget = MapWidget()
        mapWidget.commonSongData.setSongData(song)
        mapWidget.mapActionButtons.setStatusDownloadFinished()
        self.windowLoaderLayout.songPanel.songDownloadList.mapList.addSong(mapWidget)

    def addDownloaderDownloadingSongToView(self, song=SongShortInfo, d=QWebEngineDownloadItem):
        mapWidget = MapWidget()
        mapWidget.commonSongData.setSongData(song)
        mapWidget.mapActionButtons.setStatusDownloading()
        d.downloadProgress.connect(mapWidget.commonSongData.mapSizeLabel.updateSize)
        self.windowLoaderLayout.songPanel.songDownloadList.mapList.addSong(mapWidget)


class BrowserBackend(AppBackendAction):
    songListBackend = SongListBackend
    browser = QBrowserWidget
    def setup(self):
        self.browser = QBrowserWidget(self.onDownloadRequest)
        #self.browser.page().profile().dow
        self.windowLoaderLayout.browserWidget = self.browser
        self.windowLoaderLayout.initWidgets()
        self.songListBackend = SongListBackend(self.windowLoaderLayout)

    def onDownloadRequest(self, d=QWebEngineDownloadItem):
        song = self.getSongFromDownloadItem(d)

        print("Download Requested {}".format(song.fileName))

        if FileManager.isAcceptableFormat(song.fileName):
            if not FileManager.isFileExist(song.fileName):
                print("Download accepted!")
                song.songStatus = song.SongStatus.downloading
                d.setPath(song.songPath)
                d.accept()

                self.songListBackend.addDownloaderDownloadingSongToView(song, d)

            else:
                d.cancel()
                print("Download canceled, File is already exist")

        else:
            d.cancel()
            print("Download canceled, not Acceptable Format!")

        pass

    def getSongFromDownloadItem(self, d=QWebEngineDownloadItem):
        song = SongShortInfo()
        song.loadData(FileManager.cleanFileName(d.suggestedFileName()))
        song.songSize = d.receivedBytes()
        return song

