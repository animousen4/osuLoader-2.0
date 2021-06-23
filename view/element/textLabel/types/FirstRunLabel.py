import ResourceNavigator
from view.element.textLabel.LabelTypes import LargeLabel

class FirstRunLabel(LargeLabel):
    def __init__(self):
        super(FirstRunLabel, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.labelTextFirstRun)