from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from view.element.textLabel.types.FirstRunLabel import FirstRunLabel
from view.widget.pathSelector.PathSelectorWidget import PathSelectorWidget


class OsuPathSelectorWindowLayout(QVBoxLayout):
    pathSelector = PathSelectorWidget

    def __init__(self):
        super(OsuPathSelectorWindowLayout, self).__init__()

        firstRunLabel = FirstRunLabel()

        #self.pathSelector = PathSelectorWidget(bp)

        self.setAlignment(Qt.AlignHCenter)

        self.addWidget(firstRunLabel)

        #self.addWidget(self.pathSelector)

