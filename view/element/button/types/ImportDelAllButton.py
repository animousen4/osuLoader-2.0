import ResourceNavigator
from view.element.button.ButtonTypes import MediumButton


class ImportDelAllButton(MediumButton):
    pass


class ImportAllButton(ImportDelAllButton):
    def __init__(self):
        super(ImportAllButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonImportAllText)


class DeleteAllButton(ImportDelAllButton):
    def __init__(self):
        super(DeleteAllButton, self).__init__()
        self.setText(ResourceNavigator.Variables.Strings.buttonDeleteAllText)
