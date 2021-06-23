import ResourceNavigator
from view.element.inputLabel.InputLabelTypes import SimpleInputLabel


class InputLabelSelectPath(SimpleInputLabel):
    def __init__(self):
        super(InputLabelSelectPath, self).__init__()
        self.setToolTip(ResourceNavigator.Variables.Strings.labelInputOsuPathTip)