from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout

from back.objects.song.Song import SongShortInfo


class MapWidget(QFrame):
    song = SongShortInfo

    def __init__(self, s=SongShortInfo):
        super(MapWidget, self).__init__()
        self.song = s

        self.initWidget()

    def initWidget(self):
        horizontalLayout = QHBoxLayout()



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
