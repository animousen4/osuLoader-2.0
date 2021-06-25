import ResourceNavigator
from view.element.inputLabel.InputLabelTypes import SimpleInputLabel


class InputLabelSelectPath(SimpleInputLabel):
    def __init__(self, act):
        super(InputLabelSelectPath, self).__init__()
        self.setToolTip(ResourceNavigator.Variables.Strings.labelInputOsuPathTip)
        self.textEdited.connect(lambda state, a=act: act())