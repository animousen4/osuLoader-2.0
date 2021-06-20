import os
import zipfile

import ResourceNavigator
from back.osu.parser.OsuSongParser import OsuSongParser


class SongShortInfo:
    fileName = "fileName"
    songName = "songName"
    songPath = "songPath"
    songSize = -1

    def loadData(self, fName):
        self.fileName = fName
        self.songName = self.fileName.replace(".{}".format(ResourceNavigator.Local.Song.format), "")
        self.songSize = os.path.getsize(ResourceNavigator.Local.Path.songsPath + self.fileName)
        self.songPath = ResourceNavigator.Local.Path.songsPath + self.fileName


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
