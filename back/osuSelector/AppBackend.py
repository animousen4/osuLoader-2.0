from PyQt5.QtWidgets import QFileDialog

import OsuLoader2Properties
import ResourceNavigator
from back.fileManager import FileManager
from view.widget.pathSelector.PathSelectorWidget import PathSelectorWidget
from view.window.osuLoader.layout.OsuLoaderWindowLayout import OsuLoaderWindowLayout
from view.window.osuPathSelector.layout.OsuPathSelectorWindowLayout import OsuPathSelectorWindowLayout

class Layout:
    layout = OsuPathSelectorWindowLayout


class AppBackendInit:
    layout = OsuPathSelectorWindowLayout

    def __init__(self, layout=OsuPathSelectorWindowLayout):
        self.layout = layout
        self.preInit()

    def preInit(self):
        Layout.layout = self.layout
        SelectorBackend()

    def postInit(self):
        pass


class AppBackendAction:

    def __init__(self):
        self.setup()

    def setup(self):
        pass


class SelectorBackend(AppBackendAction):
    nextButtonAvailable = False
    folderPath = "folderPath"

    class BindPack:
        onOpenExplorer = None
        onNext = None
        onClose = None

    def setup(self):
        bp = self.getBP()

        Layout.layout.addWidget(PathSelectorWidget(bp))
        pass

    def getBP(self):
        bp = self.BindPack()
        bp.onOpenExplorer = self.onOpenExplorerClick
        bp.onNext = self.onNextClick
        bp.onClose = self.onCloseClick

        return bp

    def onOpenExplorerClick(self):
        print("Op explorer")
        folderPath= QFileDialog.getExistingDirectory(None, ResourceNavigator.Variables.Strings.labelTextFirstRunDialog)
        #Layout.layout.pathSelector.inputLabelSelectPath.setText(0, folderPath)
        #here
        if FileManager.isOsuFolder(folderPath):
            self.folderPath = folderPath
            self.nextButtonAvailable = True
            print("Found osu folder!")
            self.nextButtonAvailable = True

        else:
            print("Not osu folder!")
            self.nextButtonAvailable = False
        pass
    def onEdit(self):
        pass


    def onNextClick(self):
        print("Saving changes...")
        OsuLoader2Properties.Properties.app.osu.osuPath = self.folderPath
        FileManager.PropertiesLoader.saveProperties(None)
        pass

    def onCloseClick(self):
        pass