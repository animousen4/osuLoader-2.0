from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout

from back.objects.song.Song import SongShortInfo
from view.element.textLabel.types.MapLabel import MapSizeLabel, MapNameLabel


class MapWidget(QFrame):
    song = SongShortInfo

    mapNameLabel = MapNameLabel

    mapSizeLabel = MapSizeLabel

    def __init__(self, s=SongShortInfo):
        super(MapWidget, self).__init__()
        self.song = s

        self.initWidget()

    def initWidget(self):
        horizontalLayout = QHBoxLayout()

        self.mapNameLabel = MapNameLabel()

        self.mapSizeLabel = MapSizeLabel()

        #here





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
