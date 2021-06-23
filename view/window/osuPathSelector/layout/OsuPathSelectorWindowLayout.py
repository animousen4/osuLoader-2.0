from PyQt5.QtWidgets import QVBoxLayout

from view.element.textLabel.types.FirstRunLabel import FirstRunLabel


class OsuPathSelectorWindowLayout(QVBoxLayout):
    def __init__(self):
        super(OsuPathSelectorWindowLayout, self).__init__()

        self.addWidget(FirstRunLabel())

