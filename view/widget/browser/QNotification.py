from QNotifications import QNotificationArea


class AbstractQNotification(QNotificationArea):
    timeout = 2000
    fadeInTime = 200
    fadeOutTime = 400

    def __init__(self, targetWidget, *args, **kwargs):
        super().__init__(targetWidget, *args, **kwargs)

        self.setEntryEffect('fadeIn', self.fadeInTime)
        self.setExitEffect('fadeOut', self.fadeOutTime)

    def showInfo(self, message):
        self.display(message, 'info', self.timeout)


class BrowserNotification(AbstractQNotification):
    def __init__(self, targetWidget, *args, **kwargs):
        super().__init__(targetWidget, *args, **kwargs)