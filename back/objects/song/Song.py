import os
import zipfile

from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem

import ResourceNavigator
from back.osu.parser.OsuSongParser import OsuSongParser


class SongShortInfo:
    d = QWebEngineDownloadItem
    class SongStatus:
        downloadFinished = 0
        downloading = 1
    songStatus = SongStatus.downloadFinished
    fileName = "fileName"
    songName = "songName"
    songPath = "songPath"
    songSize = -1

    def loadData(self, fName):
        self.fileName = fName
        self.songName = self.fileName.replace(".{}".format(ResourceNavigator.Local.Song.format), "")
        try:
            self.songSize = os.path.getsize(ResourceNavigator.Local.Path.songPath + self.fileName)
        except Exception:
            self.songSize = -1
        self.songPath = ResourceNavigator.Local.Path.songPath + self.fileName


class SongFullInfo(SongShortInfo):
    songTempFilePath = "songTempFilePath"
    songMusicFilePath = "songMusicFilePath"
    songPicturePreviewPath = "songPicturePreviewPath"

    def loadData(self, fileName):
        super(SongFullInfo, self).loadData(fileName)

        zipExtractor = zipfile.ZipFile(self.songPath)
        zipExtractor.extractall(ResourceNavigator.Local.Path.tempPath)
        zipExtractor.close()

        self.songTempFilePath = ResourceNavigator.Local.Path.tempPath + self.fileName

        osuSongParser = OsuSongParser()
