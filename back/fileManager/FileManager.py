import json
import os

import OsuLoader2Properties
import ResourceNavigator
from back.objects.song.Song import SongShortInfo


def cleanFileName(fileName=str):
    fileName.replace(":", "").replace("\\", "").replace("/", "").replace("*", "").replace("?", "").replace('"', "") \
        .replace("|", "").replace(">", "").replace("<", "")
    return fileName


def isAcceptableFormat(fileName):
    if fileName.__contains__(".{}".format(ResourceNavigator.Local.Song.format)):
        return True

def isFileExist(fileName):
    if os.path.isfile("{}{}".format(ResourceNavigator.Local.Path.songPath, fileName)) or os.path.isfile("{}{}.{}".format(ResourceNavigator.Local.Path.songPath, fileName, "download")):
        return True
    else:
        return False

def deleteSong(song=SongShortInfo):
    os.remove(song.songPath)

def importSong(song=SongShortInfo):
    pass


class PropertiesLoader:
    def loadProperties(self):
        f = open(ResourceNavigator.PropertiesNavigator.pathOsuLoaderPropertiesJSON, "r")
        JSON = json.loads(f.read())
        OsuLoader2Properties.app.window.windowTitle = JSON['app']['window']['windowTitle']
        OsuLoader2Properties.app.window.windowResolution.x = JSON['app']['window']['windowResolution']['x']
        OsuLoader2Properties.app.window.windowResolution.y = JSON['app']['window']['windowResolution']['y']
        OsuLoader2Properties.osu.osuPath = JSON['app']['osu']['osuPath']

class LoaderLevelManager:
    songList = []

    def loadLoaderLevels(self):
        print("Loading saved maps...")

        simpleFileList = os.listdir(ResourceNavigator.Local.Path.songPath)

        for file in simpleFileList:
            if isAcceptableFormat(file):
                song = SongShortInfo()
                song.loadData(file)
                self.songList.append(song)
                print("\tMap: {}".format(file))
        return self.songList


class OsuLevelManager:
    pass

