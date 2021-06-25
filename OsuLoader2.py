import os
import sys

from PyQt5.QtWidgets import QApplication

import OsuLoader2Properties
from back.fileManager import FileManager
from view.window.osuLoader import OsuLoaderWindow
from view.window.osuPathSelector import OsuPathSelectorWindow
def restart():
    #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    os.system("python OsuLoader2.py")
def main():
    print("Starting osu!Loader 2.0 ...")
    fileChecker = FileManager.FileChecker()
    fileChecker.startCheck()

    FileManager.PropertiesLoader.loadProperties(None)

    app = QApplication(sys.argv)
    if FileManager.isAvailableOsuPath():
        print("path is defined")
        window = OsuLoaderWindow.OsuLoaderWindow()
    else:
        print("path isn't available")
        window = OsuPathSelectorWindow.OsuPathSelectorWindow()
    app.exec_()
    pass


if __name__ == "__main__":
    main()
