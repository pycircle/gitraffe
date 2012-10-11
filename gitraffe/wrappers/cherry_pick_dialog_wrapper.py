from PyQt4.QtGui import QDialog, QListWidgetItem, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL
from layouts.delete_branch_dialog import Ui_DeleteBranchDialog
from git import get_local_branches, get_current_branch, cherry_pick

class CherryPickDialogWrapper(QDialog):
    def __init__(self, commit, parent=None):
        QDialog.__init__(self)
        self.commit = commit
        self.parent = parent
        self.ui = Ui_DeleteBranchDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Cherry pick')
        self.list_branches()
        QObject.connect(self, SIGNAL('accepted()'), self.cherry_pick)

    def list_branches(self):
        branches = get_local_branches()
        for branch in branches:
            QListWidgetItem(branch, self.ui.branches2delListWidget)

    def cherry_pick(self):
        item = self.ui.branches2delListWidget.currentItem()
        if item == None:
            QMessageBox.critical(self, "Error", "You must choose branch to cherry pick on!", QMessageBox.Ok)
        elif get_current_branch() == item.text():
            QMessageBox.critical(self, "Error", "You can't cherry pick on currently used branch! You must choose another branch.", QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Cherry pick', cherry_pick(self.parent, item.text(), self.commit), QMessageBox.Ok)
            self.parent.refresh_graph()

