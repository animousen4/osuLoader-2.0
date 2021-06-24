import json
import os
import zipfile

from setuptools.msvc import winreg

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

def isSongExist(fileName):
    if os.path.isfile("{}{}".format(ResourceNavigator.Local.Path.songPath, fileName)) or os.path.isfile("{}{}.{}".format(ResourceNavigator.Local.Path.songPath, fileName, "download")):
        return True
    else:
        return False

def isDirExist(path):
    return os.path.isdir(path)
    pass

def isFileExist(path):
    return os.path.isfile(path)

def isAvailableOsuPath():
    if OsuLoader2Properties.Properties.app.osu.osuPath != None:
        return True
    return False

def isOsuFolder(filePath):
    if os.path.isfile(filePath + "/{}".format(ResourceNavigator.Local.Path.osuExeFileName)):
        return True
    else:
        return False
def deleteSong(song=SongShortInfo):
    os.remove(song.songPath)

def importSong(song=SongShortInfo):
    pass
def getOsuAutoPath(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)

            if winreg.QueryValueEx(asubkey, "DisplayName")[0] == "osu!":
                #print("Found!")
                iconPath = str(winreg.QueryValueEx(asubkey, "DisplayIcon")[0])
                path = iconPath.replace("\osu!.exe", "").replace("\\", "/")

                return path
        except EnvironmentError:
            continue

    return None
class PropertiesLoader:
    def loadProperties(self):
        f = open(ResourceNavigator.PropertiesNavigator.pathOsuLoaderPropertiesJSON, "r")
        JSON = json.loads(f.read())
        OsuLoader2Properties.Properties.app.window.windowTitle = JSON['app']['window']['windowTitle']
        OsuLoader2Properties.Properties.app.window.windowResolution.x = JSON['app']['window']['windowResolution']['x']
        OsuLoader2Properties.Properties.app.window.windowResolution.y = JSON['app']['window']['windowResolution']['y']
        OsuLoader2Properties.Properties.app.osu.osuPath = JSON['app']['osu']['osuPath']
        f.close()

    def saveProperties(self):

        dictionary = {
          "app": {
            "window": {
              "windowTitle": OsuLoader2Properties.Properties.app.window.windowTitle,
              "windowResolution": {
                "x": OsuLoader2Properties.Properties.app.window.windowResolution.x,
                "y": OsuLoader2Properties.Properties.app.window.windowResolution.y
              }
            },
            "osu": {
              "osuPath": OsuLoader2Properties.Properties.app.osu.osuPath
            }
          }
        }

        fileSave = json.dumps(dictionary)

        f = open(ResourceNavigator.PropertiesNavigator.pathOsuLoaderPropertiesJSON, "w")
        f.write(fileSave)
        f.close()
        #dict = OsuLoader2Properties.Properties.__dict__
        #json.JSONEncoder().encode()
            #f.write(chunk)
        #f.close()
        #JSON = json.dumps()
        #f.write(JSON)
        #f.close()
        pass

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
    def unpackSong(self, s=SongShortInfo):
        print("Extracting song: {}".format(s.songName))
        zipExtractor = zipfile.ZipFile(s.songPath)
        zipExtractor.extractall("{}/{}/{}".format(OsuLoader2Properties.Properties.app.osu.osuPath, ResourceNavigator.Local.Osu.songPath, s.songName))
        zipExtractor.close()


class FileChecker:
    def startCheck(self):
        if not isDirExist(ResourceNavigator.Local.Path.songPath):
            print("Song file is not exists: " + ResourceNavigator.Local.Path.songPath)
            try:
                os.mkdir(ResourceNavigator.Local.Path.songPath)
            except Exception:
                pass

        if not isFileExist(ResourceNavigator.PropertiesNavigator.pathOsuLoaderPropertiesJSON):
            print("Properties is not exists")
            try:
                os.mkdir(ResourceNavigator.PropertiesNavigator.pathOsuLoaderProperties)
            except Exception: pass
            f = open(ResourceNavigator.PropertiesNavigator.pathOsuLoaderPropertiesJSON, "w")
            f.write(json.dumps(ResourceNavigator.Structure.DefaultProperties.stdProperties))
            f.close()

        if not isFileExist(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSS) or not isFileExist(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSSVariables):
            print("Style file not exists")
            try:
                os.mkdir(ResourceNavigator.Local.Path.stylePath)
            except Exception: pass

            f = open(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSS, "w")
            f.write(ResourceNavigator.Structure.StyleSheet.css)
            f.close()

            f = open(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSSVariables, "w")
            f.write(ResourceNavigator.Structure.StyleSheet.variables)
            f.close()


class OsuLevelManager:
    pass

