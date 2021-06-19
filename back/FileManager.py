import os

import ResourceNavigator


class LoaderLevelManager:
    levels = []

    def __init__(self):
        pass

    def loadLoaderLevels(self):
        print("Loading saved maps...")

        songList = []

        simpleFileList = os.listdir(ResourceNavigator.Local.Path.songsPath)

        for file in simpleFileList:
            path =
            size = os.path.getsize(ResourceNavigator.Local.Path.songsPath + file)

            #songList.append()
            print("     Map: {}".format(file))
        print()
        return fileList

        pass

    pass


class OsuLevelManager:
    pass
