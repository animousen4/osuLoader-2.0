from PyQt5.QtWidgets import QFileDialog

import OsuLoader2Properties
import ResourceNavigator
from back.fileManager import FileManager
from back.osuSelector import AutoPathDetector
from view.widget.pathSelector.ActionButtonWidget import ActionButtonWidget
from view.widget.pathSelector.PathSelectorWidget import PathSelectorWidget
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

    pathSelectorWidget = PathSelectorWidget
    actionButtonWidget = ActionButtonWidget
    class BindPack:
        onOpenExplorer = None
        onNext = None
        onExit = None
        onEdit = None

    def setup(self):
        bp = self.getBP()
        self.pathSelectorWidget = PathSelectorWidget(bp)
        self.actionButtonWidget = ActionButtonWidget(bp)

        Layout.layout.addWidget(self.pathSelectorWidget)
        Layout.layout.addWidget(self.actionButtonWidget)

        self.autoFillInputLabel()

        self.updateButtonNextState()

    def autoFillInputLabel(self):
        autoPath = AutoPathDetector.getOsuPath()
        if autoPath!=None:
            self.pathSelectorWidget.inputLabelSelectPath.setText(autoPath)
            self.checkCorrectFolder()

    def checkCorrectFolder(self):
        folderPath = self.pathSelectorWidget.inputLabelSelectPath.text()
        if folderPath == "":
            self.pathSelectorWidget.hintLabel.setSimpleText(ResourceNavigator.Variables.Strings.startOsuFolderText)
            return
        if FileManager.isOsuFolder(folderPath):
            print("Found osu folder!")
            self.pathSelectorWidget.hintLabel.setSimpleText(ResourceNavigator.Variables.Strings.findOsuFolderText)
            self.folderPath = folderPath
            self.nextButtonAvailable = True

        else:
            print("Not osu folder!")
            self.pathSelectorWidget.hintLabel.setAngryText(ResourceNavigator.Variables.Strings.warnNotOsuFolderText)
            self.folderPath = "folderPath"
            self.nextButtonAvailable = False
        self.updateButtonNextState()

    def updateButtonNextState(self):
        self.actionButtonWidget.nextButton.setDisabled(not self.nextButtonAvailable)

    def getBP(self):
        bp = self.BindPack()
        bp.onOpenExplorer = self.onOpenExplorerClick
        bp.onNext = self.onNextClick
        bp.onExit = self.onExitClick
        bp.onEdit = self.onEdit

        return bp

    def onOpenExplorerClick(self):
        print("Op explorer")
        folderPath= QFileDialog.getExistingDirectory(None, ResourceNavigator.Variables.Strings.labelTextFirstRunDialog)
        print("chosen folder - {}".format(folderPath))
        self.pathSelectorWidget.inputLabelSelectPath.setText(folderPath)
        self.checkCorrectFolder()

    def onEdit(self):
        textLineEdit = self.pathSelectorWidget.inputLabelSelectPath.text()
        print("edit - {}".format(textLineEdit))
        self.checkCorrectFolder()

    def onNextClick(self):
        print("Saving changes...")
        OsuLoader2Properties.Properties.app.osu.osuPath = self.folderPath
        FileManager.PropertiesLoader.saveProperties(None)
        exit(0)

    def onExitClick(self):
        print("Exit...")
        exit(0)