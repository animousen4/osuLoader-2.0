import ResourceNavigator
from view.element.textLabel.LabelTypes import LargeLabel


class DownloadsLabel(LargeLabel):
    def __init__(self):
        super(DownloadsLabel, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.labelDownloads)
