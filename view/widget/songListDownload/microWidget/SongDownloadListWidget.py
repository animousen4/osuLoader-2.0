from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea

from back.objects.song.Song import SongShortInfo
from view.element.button.types.ActionButton import ActionButtonImport, ActionButtonDeleteFile, \
    ActionButtonCancelDownload
from view.element.progressBar.ProgressBarTypes import DownloadProgressBar
from view.element.scrollArea.SimpleScrollArea import SimpleScrollArea
from view.element.textLabel.types.MapLabel import MapSizeLabel, MapNameLabel


class CommonSongDataWidget(QFrame):
    song = SongShortInfo

    mapNameLabel = MapNameLabel

    mapSizeLabel = MapSizeLabel

    mapDownloadBar = DownloadProgressBar

    def __init__(self):
        super(CommonSongDataWidget, self).__init__()

        self.setContentsMargins(0,0,0,0)
        self.initWidget()

    def initWidget(self):
        verticalLayoutNS = QVBoxLayout()
        verticalLayoutNS.setContentsMargins(0, 0, 0, 0)
        verticalLayoutNS.setSpacing(0)
        verticalLayoutNS.setAlignment(Qt.AlignVCenter)

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

    def __init__(self, bindPack):
        super(ActionButtonPanelWidget, self).__init__()

        self.actionButtonDeleteFile = ActionButtonDeleteFile()
        self.actionButtonImport = ActionButtonImport()
        self.actionButtonCancelDownload = ActionButtonCancelDownload()

        self.initBindings(bindPack)

        self.initWidget()

    def initWidget(self):
        self.hWidgetLayout = QHBoxLayout()
        self.hWidgetLayout.setAlignment(Qt.AlignRight)
        self.hWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.hWidgetLayout.setSpacing(5)
        # ...
        self.setLayout(self.hWidgetLayout)

    def initBindings(self, bindPack):
        self.actionButtonImport.clicked.connect(lambda state, s=bindPack.song: bindPack.onActionButtonImportClick(state, s))
        self.actionButtonDeleteFile.clicked.connect(lambda state, s=bindPack.song: bindPack.onActionButtonDeleteClick(state, s))
        self.actionButtonCancelDownload.clicked.connect(lambda state, s=bindPack.song: bindPack.onActionButtonCancelDownloadClick(state, s))
        pass

    def setStatusDownloading(self):
        self.hWidgetLayout.addWidget(self.actionButtonCancelDownload)

    def setStatusDownloadFinished(self):
        self.hWidgetLayout.removeWidget(self.actionButtonCancelDownload)
        self.actionButtonCancelDownload.deleteLater()
        self.hWidgetLayout.addWidget(self.actionButtonImport)
        self.hWidgetLayout.addWidget(self.actionButtonDeleteFile)


class MapWidget(QFrame):
    mapActionButtons = ActionButtonPanelWidget

    commonSongData = CommonSongDataWidget

    def __init__(self, bindPack):
        super(MapWidget, self).__init__()

        self.initWidget(bindPack)

    def initWidget(self, bindPack):
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(20)

        self.mapActionButtons = ActionButtonPanelWidget(bindPack)

        self.commonSongData = CommonSongDataWidget()

        horizontalLayout.addWidget(self.commonSongData)
        horizontalLayout.addWidget(self.mapActionButtons)

        self.setLayout(horizontalLayout)

    def onDownloadFinished(self):
        self.mapActionButtons.setStatusDownloadFinished()
        self.commonSongData.song.songStatus = SongShortInfo.SongStatus.downloadFinished
        pass


class MapListWidget(QVBoxLayout):
    def __init__(self):
        super(MapListWidget, self).__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(25)
        self.setAlignment(Qt.AlignTop)

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
