from view.element.textLabel.LabelTypes import SmallLabel


class MapLabel(SmallLabel):
    def __init__(self):
        super(MapLabel, self).__init__()


class MapNameLabel(MapLabel):
    name = str

    def setName(self, n):
        self.name = n
        self.setText(self.name)


class MapSizeLabel(MapLabel):
    currentSize = -1
    downloadSize = -1

    percent = -1

    def updateSize(self, curS, dowS):
        self.percent = round(curS / dowS * 100, 1)
        self.currentSize = curS
        self.downloadSize = dowS
        self.setText("{}/{} MB".format(curS, dowS))
