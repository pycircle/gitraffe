from PyQt4.QtGui import QDialog, QListWidgetItem
from PyQt4.QtCore import QObject, SIGNAL
from layouts.delete_branch_dialog import Ui_DeleteBranchDialog
from git import get_local_branches

class DeleteBranchDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_DeleteBranchDialog()
        self.ui.setupUi(self)
        self.list_branches()

    def list_branches(self):
        branches = get_local_branches()
        for branch in branches:
            QListWidgetItem(branch, self.ui.branches2delListWidget)
