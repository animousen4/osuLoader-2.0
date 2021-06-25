import ResourceNavigator
from view.element.button.ButtonTypes import LevelButton


class ImportDelAllButton(LevelButton):
    def __init__(self, act):
        super(ImportDelAllButton, self).__init__()
        self.clicked.connect(lambda state, a=act: act(None))

    pass


class ImportAllButton(ImportDelAllButton):
    def __init__(self, act):
        super(ImportAllButton, self).__init__(act)
        self.setText(ResourceNavigator.Variables.Strings.buttonImportAllText)


class DeleteAllButton(ImportDelAllButton):
    def __init__(self, act):
        super(DeleteAllButton, self).__init__(act)
        self.setText(ResourceNavigator.Variables.Strings.buttonDeleteAllText)
