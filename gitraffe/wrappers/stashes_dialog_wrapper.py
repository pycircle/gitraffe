from PyQt4.QtGui import QDialog, QListWidgetItem, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL
from layouts.stashes_dialog import Ui_StashesDialog
from git import stashes_list, apply_stash, drop_stash

class StashesDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_StashesDialog()
        self.ui.setupUi(self)
        QObject.connect(self.ui.applyButton, SIGNAL('clicked()'), self.apply_stash)
        QObject.connect(self.ui.dropButton, SIGNAL('clicked()'), self.drop)
        self.list_stashes()

    def list_stashes(self):
        stashes = stashes_list()
        for stash in stashes:
            QListWidgetItem(stash, self.ui.stashesListWidget)

    def error(self):
        QMessageBox.critical(self, 'Error', 'You must choose stash to apply or drop it!', QMessageBox.Ok)

    def apply_stash(self):
        item  = self.ui.stashesListWidget.currentItem()
        if item == None:
            self.error()
        elif item.isSelected() == True:
            stash = item.text().split()[0][:-1]
            apply_stash(stash)
            QMessageBox.information(self, 'Apply stash', 'Stash %s applied' % (stash), QMessageBox.Ok)
        else:
            self.error()

    def drop(self):
        item = self.ui.stashesListWidget.currentItem()
        if item == None:
            self.error()
        elif item.isSelected() == True:
            QMessageBox.information(self, 'Drop stash', drop_stash(item.text().split()[0][:-1]), QMessageBox.Ok)
            self.ui.stashesListWidget.clear()
            self.list_stashes()
        else:
            self.error()
           