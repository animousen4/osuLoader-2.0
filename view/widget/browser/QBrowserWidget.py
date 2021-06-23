from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEngineDownloadItem
from PyQt5.QtWidgets import QFrame

import ResourceNavigator
from view.widget.browser import QNotification


class QBrowserWidget(QWebEngineView):

    browserNotification = QNotification.BrowserNotification

    def __init__(self, d):
        super(QBrowserWidget, self).__init__()

        self.d = d

        self.setupBrowser()

    def setupBrowser(self):
        self.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.page().setBackgroundColor(QColor("#1f1f1f"))
        self.page().profile().downloadRequested.connect(self.d)
        self.browserNotification = QNotification.BrowserNotification(self)
        #self.downloadSignal.connect(self.fff)


    def downloadRequested(self, d=QWebEngineDownloadItem):
        print("DOWNLOAD REQUESTED!")

    def goBack(self):
        self.back()

    def goForward(self):
        self.forward()
