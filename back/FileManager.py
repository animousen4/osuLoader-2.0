import os

import ResourceNavigator
from back.objects.song.Song import SongShortInfo


class LoaderLevelManager:
    songList = []
    songFormat = ResourceNavigator.Local.Song.format

    def loadLoaderLevels(self):
        print("Loading saved maps...")

        simpleFileList = os.listdir(ResourceNavigator.Local.Path.songsPath)

        for file in simpleFileList:
            if file.__contains__(".{}".format(self.songFormat)):
                song = SongShortInfo()
                song.loadData(file)
                self.songList.append(song)
                print("\tMap: {}".format(file))
        return self.songList


class OsuLevelManager:
    pass
