from view.element.textLabel.LabelTypes import SmallLabel


class HintLabel(SmallLabel):
    def __init__(self):
        super(HintLabel, self).__init__()

    def setAngryText(self, text: str):
        self.setStyleSheet("color: red;")
        self.setText(text)

    def setSimpleText(self, text: str):
        self.setStyleSheet("color: #ababab;")
        self.setText(text)