from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QFrame

import ResourceNavigator


class QBrowserWidget(QWebEngineView):
    def __init__(self):
        super(QBrowserWidget, self).__init__()

        self.setupBrowser()

        self.onStart()

    def setupBrowser(self):
        self.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.page().setBackgroundColor(QColor("#1f1f1f"))

    def onStart(self):
        pass
        #self.loadBeatMapPage()

    def goBack(self):
        self.back()

    def goForward(self):
        self.forward()
