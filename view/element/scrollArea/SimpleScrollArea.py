from PyQt5 import QtCore
from PyQt5.QtWidgets import QScrollArea, QWidget


class SimpleScrollArea(QScrollArea):
    def __init__(self):
        super(SimpleScrollArea, self).__init__()

    def eventFilter(self, obj: QtCore.QObject, ev: QtCore.QEvent) -> bool:
        if obj == self.widget() and ev.type() == QtCore.QEvent.Type.Resize:
            self.setMaximumWidth(self.width() - self.viewport().width() + self.widget().width())
        return QScrollArea.eventFilter(self, obj, ev)

    def setWidget(self, w: QWidget) -> None:
        QScrollArea.setWidget(self, w)
        w.installEventFilter(self)
