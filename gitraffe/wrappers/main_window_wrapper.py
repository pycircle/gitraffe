from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog, QIcon, QTableWidgetItem, QAbstractItemView, QWidget
from PyQt4.QtCore import QDir, QObject, SIGNAL, Qt, QPoint
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git import check_repository, open_repository, get_graph, get_files, change_local_branch, change_remote_branch, pull, commit, push, get_local_chanegs, get_file_changes, get_current_branch
import db_adapter
import os
from layouts import main_window
from wrappers.clone_dialog_wrapper import CloneWindowWrapper
from wrappers.branches_dialog_wrapper import BranchesDialogWrapper
from wrappers.delete_branch_dialog_wrapper import DeleteBranchDialogWrapper
from wrappers.about_dialog_wrapper import AboutDialogWrapper
from wrappers.settings_dialog_wrapper import SettingsDialogWrapper
from layouts.graph_widget import GraphWidget
from layouts.defined_graph_widget import DefinedGraphWidget

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Repository list
        self.ui.listWidget.setMouseTracking(True)
        self.ui.listWidget.itemSelectionChanged.connect(self.view_repository)
        self.list_all_repositories()
        #Repository Table
        self.ui.repositoryTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.repositoryTableWidget.verticalHeader().setVisible(False)
        self.ui.repositoryTableWidget.itemSelectionChanged.connect(self.view_files)
        #Files List
        self.ui.files_listWidget.itemSelectionChanged.connect(self.view_file_changes)
        # Menu/toolbar
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionSettings, SIGNAL('triggered()'), self.settings_dialog)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
        QObject.connect(self.ui.actionDelete_repository, SIGNAL('triggered()'), self.delete_listWidgetitem)
        QObject.connect(self.ui.actionClone_repository_3, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository_2, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionPull, SIGNAL('triggered()'), self.pull)
        QObject.connect(self.ui.actionCommit, SIGNAL('triggered()'), self.commit)
        QObject.connect(self.ui.actionPush, SIGNAL('triggered()'), self.push)
        QObject.connect(self.ui.actionChange_branch, SIGNAL('triggered()'), self.change_branch_dialog)
        QObject.connect(self.ui.actionDelete_branch, SIGNAL('triggered()'), self.delete_branch_dialog)
        QObject.connect(self.ui.actionAbout_Gitraffe, SIGNAL('triggered()'), self.about_dialog)
        # Buttons
        QObject.connect(self.ui.pullButton, SIGNAL('clicked()'), self.pull)
        QObject.connect(self.ui.commitButton, SIGNAL('clicked()'), self.commit)
        QObject.connect(self.ui.pushButton, SIGNAL('clicked()'), self.push)

    def list_all_repositories(self):
        repositories = db_adapter.get_repositories()
        for repository in repositories:
            self.add_to_list(repository.name, repository.path)

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="":
            path = check_repository(directory)
            if path[0]:
                if not db_adapter.exists_repository(directory):
                    directory = path[1]
                    name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(directory))
                    if name[1]:
                        self.add_to_database(name[0], directory)
                        self.add_to_list(name[0], directory)
                else:
                    QMessageBox.critical(self, "Error", "This repository is already added", QMessageBox.Ok)
            else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)

    def add_to_database(self, name, directory):
        db_adapter.add_repository(name, directory)

    def add_to_list(self, name, directory):
        repo = QListWidgetItem(QIcon(os.path.dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), name, self.ui.listWidget)
        repo.setStatusTip(directory)
        repo.setData(Qt.UserRole, directory)
        repo.setFlags(repo.flags() | Qt.ItemIsEditable)

    def delete_listWidgetitem(self):
        if self.ui.listWidget.count()!=0:
            name = self.ui.listWidget.item(self.ui.listWidget.currentRow()).text()
            respond = QMessageBox.question(self, "Delete", 
                                           "Are you sure, that you want delete " + name,
                                           QMessageBox.Ok, QMessageBox.Cancel)
            if respond==QMessageBox.Ok:
                db_adapter.delete_repository(self.ui.listWidget.currentItem().data(Qt.UserRole))
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def graph(self):
        graph = get_graph()
        self.ui.repositoryTableWidget.setRowCount(len(graph)+1)
        item = DefinedGraphWidget('current.png')
        self.ui.repositoryTableWidget.setCellWidget(0, 0, item)
        self.ui.repositoryTableWidget.setItem(0, 2, QTableWidgetItem('Current local changes'))
        item = DefinedGraphWidget('commit-first.png')
        self.ui.repositoryTableWidget.setCellWidget(1, 0, item)
        for i in range(1, len(graph[0])):
            item = QTableWidgetItem(graph[0][i])
            self.ui.repositoryTableWidget.setItem(1, i, item)
        for i in range(1, len(graph)-1):
            item = GraphWidget(graph[i][0], graph[i+1][0])
            self.ui.repositoryTableWidget.setCellWidget(i+1, 0, item)
            for j in range(1, len(graph[i])):
                item = QTableWidgetItem(graph[i][j])
                self.ui.repositoryTableWidget.setItem(i+1, j, item)
        item = DefinedGraphWidget('commit-last.png')
        self.ui.repositoryTableWidget.setCellWidget(len(graph), 0, item)
        for i in range(1, len(graph[-1])):
            item = QTableWidgetItem(graph[-1][i])
            self.ui.repositoryTableWidget.setItem(len(graph), i, item)

    def refresh_graph(self):
        self.ui.repositoryTableWidget.clearContents()
        self.graph()

    def view_repository(self):
        path = self.ui.listWidget.currentItem().data(Qt.UserRole)
        open_repository(path)
        self.ui.repositoryTableWidget.selectRow(0)
        self.refresh_graph()

    def clone_respoitory(self):
        cwd = CloneWindowWrapper(self)
        cwd.exec_()

    def view_files(self):
        self.ui.files_listWidget.clear()
        commit = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1).text()
        if commit != "":
            files = get_files(commit)
            for flag, file in files:
                QListWidgetItem(flag+" "+file, self.ui.files_listWidget)
        elif self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 2).text() == 'Current local changes':
            files = get_local_chanegs()
            for file in files:
                QListWidgetItem(file, self.ui.files_listWidget)
        self.ui.files_listWidget.setCurrentRow(0)
            

    def get_default_branch_name(self, name):
        name = name.split('/')
        return name[1]

    def change_lcl_branch(self):
        item = self.bdw.ui.localBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            change_local_branch(item.text())

    def change_rmt_branch(self):
        item = self.bdw.ui.remoteBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            name = QInputDialog().getText(self, 'Name', 'Put your branch name:', text=self.get_default_branch_name(item.text()))
            if name[1]:
                change_remote_branch(item.text(), name[0])

    def change_branch(self):
        if self.bdw.ui.branchesTabWidget.currentIndex() == 0:
            self.change_lcl_branch()
        else:
            self.change_rmt_branch()
        self.refresh_graph()

    def change_branch_dialog(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            self.bdw = BranchesDialogWrapper(self)
            QObject.connect(self.bdw, SIGNAL('accepted()'), self.change_branch)
            self.bdw.exec_()
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before changing branch!", QMessageBox.Ok)

    def delete_branch_dialog(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            DeleteBranchDialogWrapper(self).exec_()
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before deleting branch!", QMessageBox.Ok)

    def about_dialog(self):
        AboutDialogWrapper(self).exec_()

    def pull(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            QMessageBox.information(self, "Pull", pull(), QMessageBox.Ok)
            self.refresh_graph()
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before pulling!", QMessageBox.Ok)

    def commit(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            message = QInputDialog().getText(self, 'Commit', 'Put your commit message:')
            if message[0] != '':
                QMessageBox.information(self, "Commit", commit(message[0]), QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before commiting!", QMessageBox.Ok)

    def push(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            QMessageBox.information(self, "Push", push(), QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before commiting!", QMessageBox.Ok)

    def settings_dialog(self):
        SettingsDialogWrapper(self).exec_()
    
    def view_file_changes(self):
        self.ui.diff_textBrowser.clear()
        commit = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1).text()
        comparsion = None
        if self.ui.repositoryTableWidget.currentRow()+1 != self.ui.repositoryTableWidget.rowCount():
            comparsion = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow()+1, 1).text()
        flag, path = self.ui.files_listWidget.currentItem().text().split()
        self.ui.diff_textBrowser.setText(get_file_changes(flag, path, commit, comparsion))
