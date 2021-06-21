from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget

from back.objects.song.Song import SongShortInfo
from view.element.button.types.ActionButton import ActionButtonImport, ActionButtonDeleteFile, \
    ActionButtonCancelDownload
from view.element.progressBar.ProgressBarTypes import DownloadProgressBar
from view.element.textLabel.types.MapLabel import MapSizeLabel, MapNameLabel


class CommonSongDataWidget(QFrame):
    song = SongShortInfo

    mapNameLabel = MapNameLabel

    mapSizeLabel = MapSizeLabel

    mapDownloadBar = DownloadProgressBar

    def __init__(self):
        super(CommonSongDataWidget, self).__init__()

        self.initWidget()

    def initWidget(self):
        verticalLayoutNS = QVBoxLayout()
        verticalLayoutNS.setContentsMargins(0, 0, 0, 0)
        verticalLayoutNS.setSpacing(0)

        verticalLayoutNSWidget = QWidget()

        verticalLayout = QVBoxLayout()
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(0)

        self.mapNameLabel = MapNameLabel()

        self.mapDownloadBar = DownloadProgressBar()

        self.mapSizeLabel = MapSizeLabel(self.mapDownloadBar)

        verticalLayoutNS.addWidget(self.mapNameLabel)
        verticalLayoutNS.addWidget(self.mapSizeLabel)

        verticalLayoutNSWidget.setLayout(verticalLayoutNS)

        verticalLayout.addWidget(verticalLayoutNSWidget)
        verticalLayout.addWidget(self.mapDownloadBar)

        self.setLayout(verticalLayout)

    def setSongData(self, songInfo=SongShortInfo):
        self.song = songInfo
        self.mapNameLabel.setName(self.song.songName)
        if self.song.songStatus == self.song.SongStatus.downloadFinished:
            self.mapSizeLabel.updateSize(self.song.songSize, self.song.songSize)


class ActionButtonPanelWidget(QFrame):
    hWidgetLayout = QHBoxLayout

    actionButtonDeleteFile = ActionButtonDeleteFile
    actionButtonImport = ActionButtonImport
    actionButtonCancelDownload = ActionButtonCancelDownload

    def __init__(self):
        super(ActionButtonPanelWidget, self).__init__()

        self.actionButtonDeleteFile = ActionButtonDeleteFile()
        self.actionButtonImport = ActionButtonImport()
        self.actionButtonCancelDownload = ActionButtonCancelDownload()

        self.initWidget()

    def initWidget(self):
        self.hWidgetLayout = QHBoxLayout()
        self.hWidgetLayout.setContentsMargins(0, 0, 0, 0)
        #self.hWidgetLayout.setSpacing(0)
        # ...
        self.setLayout(self.hWidgetLayout)

    def setStatusDownloading(self):
        self.hWidgetLayout.addWidget(self.actionButtonCancelDownload)

    def setStatusDownloadFinished(self):
        self.hWidgetLayout.removeWidget(self.actionButtonCancelDownload)
        self.hWidgetLayout.addWidget(self.actionButtonImport)
        self.hWidgetLayout.addWidget(self.actionButtonDeleteFile)


class MapWidget(QFrame):
    mapActionButtons = ActionButtonPanelWidget

    commonSongData = CommonSongDataWidget

    def __init__(self):
        super(MapWidget, self).__init__()

        self.initWidget()

    def initWidget(self):
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setSpacing(0)

        self.mapActionButtons = ActionButtonPanelWidget()

        self.commonSongData = CommonSongDataWidget()

        horizontalLayout.addWidget(self.commonSongData)
        horizontalLayout.addWidget(self.mapActionButtons)

        self.setLayout(horizontalLayout)
        # here


class MapListWidget(QVBoxLayout):
    def __init__(self):
        super(MapListWidget, self).__init__()
        self.setSpacing(0)

    def addSong(self, mapWidget=MapWidget):
        self.addWidget(mapWidget)
        pass


class SongDownloadListWidget(QFrame):
    mapList = MapListWidget

    def __init__(self):
        super(SongDownloadListWidget, self).__init__()

        self.mapList = MapListWidget()

        self.setLayout(self.mapList)

        #!!!! importDelButtons = ImportDelAllButtonWidget
