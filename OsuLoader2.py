import sys

from PyQt5.QtWidgets import QApplication

import OsuLoader2Properties
from back.fileManager import FileManager
from view.window.osuLoader import OsuLoaderWindow
from view.window.osuPathSelector import OsuPathSelectorWindow


def isAvailableOsuPath():
    if OsuLoader2Properties.osu.osuPath != None:
        return True
    return False
def main():
    print("Starting osu!Loader 2.0 ...")
    FileManager.PropertiesLoader.loadProperties(None)

    app = QApplication(sys.argv)
    if isAvailableOsuPath():
        window = OsuLoaderWindow.OsuLoaderWindow()
    else:
        print("path isn't available")
        window = OsuPathSelectorWindow.OsuPathSelectorWindow()
    app.exec_()
    pass


if __name__ == "__main__":
    main()
