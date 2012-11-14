from PyQt4.QtGui import QDialog, QMessageBox, QInputDialog, QListWidgetItem
from PyQt4.QtCore import QObject, SIGNAL
from layouts.branches_dialog import Ui_BranchesDialog
from git.branches import get_local_branches, get_remote_branches, change_local_branch, change_remote_branch

class BranchesDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_BranchesDialog()
        self.ui.setupUi(self)
        self.list_local_branches()
        self.list_remote_branches()
        QObject.connect(self, SIGNAL('accepted()'), self.change_branch)

    def list_local_branches(self):
        branches = get_local_branches()
        for branch in branches:
            QListWidgetItem(branch, self.ui.localBranchesListWidget)
    
    def list_remote_branches(self):
        branches = get_remote_branches()
        for branch in branches:
            QListWidgetItem(branch, self.ui.remoteBranchesListWidget)

    def error(self):
        QMessageBox.critical(self, "Error", "You must choose branch!", QMessageBox.Ok)

    def get_default_branch_name(self, name):
        name = name.split('/')
        return name[1]

    def change_lcl_branch(self):
        item = self.ui.localBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            change_local_branch(item.text())

    def change_rmt_branch(self):
        item = self.ui.remoteBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            name = QInputDialog().getText(self, 'Name', 'Put your branch name:', text=self.get_default_branch_name(item.text()))
            if name[1]:
                QMessageBox.information(self, 'Change branch', change_remote_branch(item.text(), name[0]), QMessageBox.Ok)

    def change_branch(self):
        if self.ui.branchesTabWidget.currentIndex() == 0:
            self.change_lcl_branch()
        else:
            self.change_rmt_branch()
