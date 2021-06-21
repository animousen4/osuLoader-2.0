from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout

from back.objects.song.Song import SongShortInfo
from view.element.button.types.ActionButton import ActionButtonImport, ActionButtonDeleteFIle, ActionButtonCancelDownload
from view.element.textLabel.types.MapLabel import MapSizeLabel, MapNameLabel

class ActionButtonPanelWidget(QFrame):
    hWidgetLayout = QHBoxLayout

    actionButtonDeleteFile = ActionButtonDeleteFIle
    actionButtonImport = ActionButtonImport
    actionButtonCancelDownload = ActionButtonCancelDownload

    def __init__(self):
        super(ActionButtonPanelWidget, self).__init__()

        self.actionButtonDeleteFile = ActionButtonDeleteFIle()
        self.actionButtonImport = ActionButtonImport()
        self.actionButtonCancelDownload = ActionButtonCancelDownload()

        self.initWidget()

    def initWidget(self):
        self.hWidgetLayout = QHBoxLayout()
        #...
        self.setLayout(self.hWidgetLayout)

    def setStatusDownloading(self):
        self.hWidgetLayout.addWidget(self.actionButtonCancelDownload)


    def setStatusDownloadFinished(self):
        self.hWidgetLayout.removeWidget(self.actionButtonCancelDownload)
        self.hWidgetLayout.addWidget(self.actionButtonImport)
        self.hWidgetLayout.addWidget(self.actionButtonDeleteFile)

class MapWidget(QFrame):
    song = SongShortInfo

    mapNameLabel = MapNameLabel

    mapSizeLabel = MapSizeLabel

    def __init__(self):
        super(MapWidget, self).__init__()

        self.initWidget()

    def initWidget(self):
        horizontalLayout = QHBoxLayout()

        self.mapNameLabel = MapNameLabel()

        self.mapSizeLabel = MapSizeLabel()

        #here
    def fillDataMapWidget(self, songInfo=SongShortInfo):
        self.song = songInfo


class MapListWidget(QVBoxLayout):
    def __init__(self):
        super(MapListWidget, self).__init__()

    def addSong(self, mapWidget):
        self.addWidget(mapWidget)
        pass


class SongDownloadListWidget(QFrame):
    mapList = QVBoxLayout

    def __init__(self):
        super(SongDownloadListWidget, self).__init__()

        self.mapList = MapListWidget()

        self.setLayout(self.mapList)
