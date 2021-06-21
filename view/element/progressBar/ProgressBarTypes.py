from PyQt5.QtWidgets import QProgressBar


class DownloadProgressBar(QProgressBar):
    def __init__(self):
        super(DownloadProgressBar, self).__init__()
        self.setRange(0, 100)
        self.setTextVisible(False)
        self.setFixedHeight(15)
