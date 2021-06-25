from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem

import ResourceNavigator
from back.fileManager import FileManager
from back.fileManager.FileManager import LoaderLevelManager
from back.objects.song.Song import SongShortInfo
from view.widget.browser.QBrowserWidget import QBrowserWidget
from view.widget.songListDownload.QSongListDownloadPanel import QSongListDownloadPanel
from view.widget.songListDownload.microWidget.SongDownloadListWidget import MapWidget
from view.window.osuLoader.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout


class AppBackendInit:
    layout = OsuLoaderWindowLayout

    def __init__(self, layout=OsuLoaderWindowLayout):
        self.layout = layout
        self.preInit()

    def preInit(self):
        Layout.windowLoaderLayout = self.layout
        BrowserBackend(self.layout)
        OnStart(self.layout)
        Layout.windowLoaderLayout.initWidgets()


    def postInit(self):
       pass


class AppBackendAction:
    windowLoaderLayout = OsuLoaderWindowLayout

    def __init__(self, layout=OsuLoaderWindowLayout):
        self.windowLoaderLayout = layout
        self.setup()

    def setup(self):
        pass


class Layout:
    windowLoaderLayout = OsuLoaderWindowLayout

    def findWidgetBySong(s: SongShortInfo):
        count = Layout.windowLoaderLayout.songPanel.songDownloadList.mapList.count()
        for i in range(count):
            widget = Layout.windowLoaderLayout.songPanel.songDownloadList.mapList.itemAt(i).widget()
            if widget.commonSongData.song.songPath == s.songPath:
                return widget
        return None

    def getAllSongWidgets(s=None):
        count = Layout.windowLoaderLayout.songPanel.songDownloadList.mapList.count()
        widgets = []
        for i in range(count):
            widget = Layout.windowLoaderLayout.songPanel.songDownloadList.mapList.itemAt(i).widget()
            #if widget.commonSongData.song.songStatus!= SongShortInfo.SongStatus.downloading:
            widgets.append(widget)
        return widgets

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
    class ActionButtonController:
        class BindPackSongItem:
            song = SongShortInfo

            onActionButtonImportClick = None
            onActionButtonCancelDownloadClick = None
            onActionButtonDeleteClick = None

        class BindPackBigActionButtons:
            onImportAll = None
            onDeleteAll = None


        mapWidget = MapWidget

        def __init__(self, mapWidget):
            self.mapWidget = mapWidget

        def onActionButtonImportClick(self, s):
            print("Import - {}".format(s.fileName))
            loaderLevelManager = LoaderLevelManager()
            loaderLevelManager.unpackSong(s)
            Layout.findWidgetBySong(s).deleteLater()

        def onActionButtonCancelDownloadClick(self, s):
            print("Cancel download - {}".format(s.fileName))
            s.d.cancel()
            Layout.findWidgetBySong(s).deleteLater()

        def onActionButtonDeleteClick(self, s=SongShortInfo):
            print("Delete file - {}".format(s.fileName))
            FileManager.deleteSong(s)
            Layout.findWidgetBySong(s).deleteLater()

        def onImportAllClick(self):
            print("Imp all")
            widgets = Layout.getAllSongWidgets(None)
            for w in widgets:
                if w.commonSongData.song.songStatus!= SongShortInfo.SongStatus.downloading:
                    w.mapActionButtons.actionButtonImport.click()
            pass

        def onDelAllClick(self):
            print("Del all")
            widgets = Layout.getAllSongWidgets(None)
            for w in widgets:
                if w.commonSongData.song.songStatus != SongShortInfo.SongStatus.downloading:
                    w.mapActionButtons.actionButtonDeleteFile.click()
                else:
                    w.mapActionButtons.actionButtonCancelDownload.click()
            pass

    def setup(self):
        self.songPanel = QSongListDownloadPanel(self.getBigBindings())
        self.windowLoaderLayout.songPanel = self.songPanel

    def getSmallBindings(self, s=SongShortInfo):
        bindPack = self.ActionButtonController.BindPackSongItem()

        bindPack.onActionButtonDeleteClick = self.ActionButtonController.onActionButtonDeleteClick
        bindPack.onActionButtonCancelDownloadClick = self.ActionButtonController.onActionButtonCancelDownloadClick
        bindPack.onActionButtonImportClick = self.ActionButtonController.onActionButtonImportClick
        bindPack.song = s

        return bindPack

    def getBigBindings(self):
        bindPack = self.ActionButtonController.BindPackBigActionButtons()
        bindPack.onImportAll = self.ActionButtonController.onImportAllClick
        bindPack.onDeleteAll = self.ActionButtonController.onDelAllClick

        return bindPack

    def addDownloaderSongToView(self, song=SongShortInfo):
        mapWidget = MapWidget(self.getSmallBindings(song))
        mapWidget.commonSongData.setSongData(song)
        mapWidget.mapActionButtons.setStatusDownloadFinished()

        self.windowLoaderLayout.songPanel.songDownloadList.mapList.addSong(mapWidget)

    def addDownloaderDownloadingSongToView(self, song=SongShortInfo, d=QWebEngineDownloadItem):
        mapWidget = MapWidget(self.getSmallBindings(song))
        mapWidget.commonSongData.setSongData(song)
        mapWidget.mapActionButtons.setStatusDownloading()
        song.d = d
        d.downloadProgress.connect(mapWidget.commonSongData.mapSizeLabel.updateSize)
        d.finished.connect(mapWidget.onDownloadFinished)
        self.windowLoaderLayout.songPanel.songDownloadList.mapList.addSong(mapWidget)


class BrowserBackend(AppBackendAction):
    songListBackend = SongListBackend
    browser = QBrowserWidget

    def setup(self):
        self.browser = QBrowserWidget(self.onDownloadRequest)
        # self.browser.page().profile().dow
        self.windowLoaderLayout.browserWidget = self.browser
        #self.windowLoaderLayout.initWidgets()
        self.songListBackend = SongListBackend(self.windowLoaderLayout)

    def onDownloadRequest(self, d=QWebEngineDownloadItem):
        song = self.getSongFromDownloadItem(d)

        print("Download Requested {}".format(song.fileName))

        if FileManager.isAcceptableFormat(song.fileName):
            if not FileManager.isSongExist(song.fileName):
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
