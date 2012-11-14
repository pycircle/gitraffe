from PyQt4.QtGui import QDialog, QListWidgetItem, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL
from layouts.delete_branch_dialog import Ui_DeleteBranchDialog
from git.branches import get_local_branches, get_current_branch, delete_branch

class DeleteBranchDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_DeleteBranchDialog()
        self.ui.setupUi(self)
        self.list_branches()
        QObject.connect(self, SIGNAL('accepted()'), self.delete_branch)

    def list_branches(self):
        branches = get_local_branches()
        for branch in branches:
            QListWidgetItem(branch, self.ui.branches2delListWidget)

    def delete_branch(self):
        item = self.ui.branches2delListWidget.currentItem()
        print(get_current_branch())
        print(item.text())
        print(get_current_branch() == item.text())
        if item == None:
            QMessageBox.critical(self, "Error", "You must choose branch to delete!", QMessageBox.Ok)
        elif get_current_branch() == item.text():
            QMessageBox.critical(self, "Error", "You can't delete currently used branch! If you want to delete it, you must change branch first.", QMessageBox.Ok)
        else:
            delete_branch(item.text())
