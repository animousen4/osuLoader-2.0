from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEngineDownloadItem
from PyQt5.QtWidgets import QFrame

import ResourceNavigator


class QBrowserWidget(QWebEngineView):

    def __init__(self, d):
        super(QBrowserWidget, self).__init__()

        self.dd = d

        self.setupBrowser()

    def setupBrowser(self):
        self.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.page().setBackgroundColor(QColor("#1f1f1f"))
        self.page().profile().downloadRequested.connect(self.dd)
        #self.downloadSignal.connect(self.fff)


    def downloadRequested(self, d=QWebEngineDownloadItem):
        print("DOWNLOAD REQUESTED!")
    def fff(self):
        print("FFFF")

    def goBack(self):
        self.back()

    def goForward(self):
        self.forward()
