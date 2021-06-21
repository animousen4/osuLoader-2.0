from view.element.progressBar.ProgressBarTypes import DownloadProgressBar
from view.element.textLabel.LabelTypes import SmallLabel


class MapLabel(SmallLabel):
    def __init__(self):
        super(MapLabel, self).__init__()
        self.setWordWrap(True)


class MapNameLabel(MapLabel):
    name = str

    def setName(self, n):
        self.name = n
        self.setText(self.name)


class MapSizeLabel(MapLabel):
    mapDownloadBar = DownloadProgressBar
    currentSize = -1
    downloadSize = -1

    percent = -1

    def __init__(self, mapDownloadBar):
        super(MapSizeLabel, self).__init__()
        self.setWordWrap(False)
        self.mapDownloadBar = mapDownloadBar

    def updateSize(self, curS, dowS):
        self.percent = round(curS / dowS * 100, 1)
        self.currentSize = curS
        self.downloadSize = dowS
        self.setText("{}% - {}/{} MB".format(self.percent, round(curS / 1000000, 1), round(dowS / 1000000, 1)))
        self.mapDownloadBar.setValue(int(self.percent))
        if int(self.percent)==100:
            self.mapDownloadBar.deleteLater()
