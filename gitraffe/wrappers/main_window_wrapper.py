from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog, QIcon ,QTableWidgetItem, QAbstractItemView, QWidget, QMenu, QAction, QHeaderView
from PyQt4.QtCore import QDir, QObject, SIGNAL, Qt, QPoint
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git.repository import check_repository, open_repository
from git.commit_history import get_commits, get_graph, get_files
from git.commit import git_add, git_rm, git_reset_head, git_rm_cached, git_check_out, clean, get_unstaged_files, get_staged_files, commit
from git.branches import create_branch
from git.remote import pull, push
from git.file_diff import get_staged_file_changes, get_unstaged_file_changes
from git.stash import stash
import db_adapter
from os.path import dirname, basename
from layouts import main_window
from wrappers.clone_dialog_wrapper import CloneWindowWrapper
from wrappers.branches_dialog_wrapper import BranchesDialogWrapper
from wrappers.delete_branch_dialog_wrapper import DeleteBranchDialogWrapper
from wrappers.about_dialog_wrapper import AboutDialogWrapper
from wrappers.settings_dialog_wrapper import SettingsDialogWrapper
from wrappers.cherry_pick_dialog_wrapper import CherryPickDialogWrapper
from wrappers.stashes_dialog_wrapper import StashesDialogWrapper
from layouts.graph_widget import GraphWidget, FirstGraphWidget, LastGraphWidget
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
        self.ui.repositoryTableWidget.itemSelectionChanged.connect(self.check_table_line)
        #Files List
        self.ui.files_listWidget.itemSelectionChanged.connect(self.view_file_changes)
        self.ui.Unstaged_listwidget.itemSelectionChanged.connect(self.view_current_unstaged_file_changes)
        self.ui.Staged_listWidget.itemSelectionChanged.connect(self.view_current_staged_file_changes)
        #Un/staged_listWidget
        self.ui.Staged_listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ui.Unstaged_listwidget.setSelectionMode(QAbstractItemView.MultiSelection)
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
        QObject.connect(self.ui.actionPush, SIGNAL('triggered()'), self.push)
        QObject.connect(self.ui.actionChange_branch, SIGNAL('triggered()'), self.change_branch_dialog)
        QObject.connect(self.ui.actionDelete_branch, SIGNAL('triggered()'), self.delete_branch_dialog)
        QObject.connect(self.ui.actionCreate_branch, SIGNAL('triggered()'), self.create_branch)
        QObject.connect(self.ui.actionAbout_Gitraffe, SIGNAL('triggered()'), self.about_dialog)
        QObject.connect(self.ui.actionRefresh, SIGNAL('triggered()'), self.view_repository)
        QObject.connect(self.ui.actionStashes, SIGNAL('triggered()'), self.stashes)
        # Buttons
        QObject.connect(self.ui.pullButton, SIGNAL('clicked()'), self.pull)
        QObject.connect(self.ui.pullButton_2, SIGNAL('clicked()'), self.pull)
        QObject.connect(self.ui.pushButton, SIGNAL('clicked()'), self.push)
        QObject.connect(self.ui.pushButton_2, SIGNAL('clicked()'), self.push)
        QObject.connect(self.ui.stageButton_2, SIGNAL('clicked()'), self.stage_files)
        QObject.connect(self.ui.unstageButton_2, SIGNAL('clicked()'), self.unstage_files)
        QObject.connect(self.ui.discardButton_2, SIGNAL('clicked()'), self.discard_files)
        QObject.connect(self.ui.commitButton_2, SIGNAL('clicked()'), self.commit_files)
        QObject.connect(self.ui.stashButton_2, SIGNAL('clicked()'), self.stash)
        # Widgets
        self.ui.repositoryTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.repositoryTableWidget.customContextMenuRequested.connect(self.cherry_pick_menu)
        header = self.ui.repositoryTableWidget.horizontalHeader()
        for i in range(1, 5):
            header.setResizeMode(i, QHeaderView.Stretch)

    def list_all_repositories(self):
        repositories = db_adapter.get_repositories()
        for repository in repositories:
            self.add_to_list(repository.name, repository.path)

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="":
            if check_repository(directory):
                if not db_adapter.exists_repository(directory):
                    name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=basename(directory))
                    if name[1]:
                        self.add_to_database(name[0], directory)
                        self.add_to_list(name[0], directory)
                else:
                    QMessageBox.critical(self, "Error", "This repository is already added", QMessageBox.Ok)
            else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)

    def add_to_database(self, name, directory):
        db_adapter.add_repository(name, directory)

    def add_to_list(self, name, directory):
        repo = QListWidgetItem(QIcon(dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), name, self.ui.listWidget)
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
                self.ui.repositoryTableWidget.setRowCount(0)
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def graph(self):
        graph = get_graph()
        commits = get_commits()
        self.ui.repositoryTableWidget.setRowCount(len(commits)+1)
        item = DefinedGraphWidget('current.png')
        self.ui.repositoryTableWidget.setCellWidget(0, 0, item)
        self.ui.repositoryTableWidget.setItem(0, 2, QTableWidgetItem('Current local changes'))
        max_size = 30
        if len(commits) > 0:
            item = FirstGraphWidget(graph[0])
            self.ui.repositoryTableWidget.setCellWidget(1, 0, item)
            for i in range(len(commits[0])):
                item = QTableWidgetItem(commits[0][i])
                self.ui.repositoryTableWidget.setItem(1, i+1, item)
            for i in range(1, len(graph)-1):
                item = GraphWidget(graph[i], None, graph[i-1])
                self.ui.repositoryTableWidget.setCellWidget(i+1, 0, item)
                if item.size > max_size:
                    max_size = item.size
                for j in range(len(commits[i])):
                    item = QTableWidgetItem(commits[i][j])
                    self.ui.repositoryTableWidget.setItem(i+1, j+1, item)
            item = LastGraphWidget(graph[-1])
            self.ui.repositoryTableWidget.setCellWidget(len(graph), 0, item)
            for i in range(len(commits[-1])):
                item = QTableWidgetItem(commits[-1][i])
                self.ui.repositoryTableWidget.setItem(len(graph), i+1, item)
        self.ui.repositoryTableWidget.horizontalHeader().resizeSection(0, max_size)

    def refresh_graph(self):
        self.ui.repositoryTableWidget.clearContents()
        self.graph()

    def view_repository(self):
        item = self.ui.listWidget.currentItem()
        if item != None:
            path = item.data(Qt.UserRole)
            open_repository(path)
            self.graph()
            if self.ui.repositoryTableWidget.currentRow() == 0:
                self.view_current_changes()
            self.ui.repositoryTableWidget.selectRow(0)

    def clone_respoitory(self):
        cwd = CloneWindowWrapper(self)
        cwd.exec_()

    def check_table_line(self):
        if self.ui.repositoryTableWidget.currentRow() == 0:
            self.view_current_changes()
        else:
            self.view_files()

    def view_current_changes(self):
        self.ui.bottomwidgets.setCurrentIndex(1)
        self.ui.Unstaged_listwidget.clear()
        self.ui.Staged_listWidget.clear()
        for un_file in get_unstaged_files():
            if len(un_file)!=0:
                QListWidgetItem(' '.join(un_file), self.ui.Unstaged_listwidget)
        for s_file in get_staged_files():
            if len(s_file)!=0:
                QListWidgetItem(' '.join(s_file), self.ui.Staged_listWidget)

    def view_files(self):
        self.ui.bottomwidgets.setCurrentIndex(0)
        self.ui.files_listWidget.clear() #makes view_file_changes
        commit = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1)
        if commit != None:
            files = get_files(commit.text())
            try:
                for flag, com_file in files:
                    QListWidgetItem(flag + " " + com_file, self.ui.files_listWidget)
            except ValueError:
                pass
        if self.ui.files_listWidget.count(): self.ui.files_listWidget.setCurrentRow(0)
        else: self.view_file_changes()

    def change_branch_dialog(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            self.bdw = BranchesDialogWrapper(self)
            QObject.connect(self.bdw, SIGNAL('accepted()'), self.refresh_graph)
            self.bdw.exec_()
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before changing branch!", QMessageBox.Ok)

    def delete_branch_dialog(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            DeleteBranchDialogWrapper(self).exec_()
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before deleting branch!", QMessageBox.Ok)

    def create_branch(self):
        if self.ui.listWidget.currentItem().isSelected() == True:
            name = QInputDialog.getText(self, 'Name', 'Put your new branch name:')
            if name[1]:
                QMessageBox.information(self, 'Create branch', create_branch(self, name[0]), QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Error", "You must choose repository before creating branch!", QMessageBox.Ok)

    def about_dialog(self):
        AboutDialogWrapper(self).exec_()

    def pull(self):
        def error():
            QMessageBox.critical(self, "Error", "You must choose repository before pulling!", QMessageBox.Ok)
        if self.ui.listWidget.currentItem() != None:
            if self.ui.listWidget.currentItem().isSelected() == True:
                QMessageBox.information(self, "Pull", pull(self), QMessageBox.Ok)
                self.refresh_graph()
            else:
                error()
        else:
            error()

    def push(self):
        def error():
            QMessageBox.critical(self, "Error", "You must choose repository before pushing!", QMessageBox.Ok)
        if self.ui.listWidget.currentItem() != None:
            if self.ui.listWidget.currentItem().isSelected():
                QMessageBox.information(self, "Push", push(self), QMessageBox.Ok)
                self.view_repository()
            else:
                error()
        else:
            error()

    def settings_dialog(self):
        SettingsDialogWrapper(self).exec_()

    def view_current_staged_file_changes(self):
        self.ui.diff_local_textBrowser.clear()
        staged = self.ui.Staged_listWidget.currentItem()
        comparsion = self.ui.repositoryTableWidget.item(1,1).text()
        if staged and staged.isSelected():
            flag, path = staged.text().split(None, 1)
            path = "\ ".join(path.split())
            self.ui.diff_local_textBrowser.setText(get_staged_file_changes(flag, path, comparsion = comparsion))

    def view_current_unstaged_file_changes(self):
        self.ui.diff_local_textBrowser.clear()
        unstaged = self.ui.Unstaged_listwidget.currentItem()
        comparsion = self.ui.repositoryTableWidget.item(1,1).text()
        if unstaged and unstaged.isSelected():
            flag, path = unstaged.text().split(None, 1)
            path = "\ ".join(path.split())
            self.ui.diff_local_textBrowser.setText(get_unstaged_file_changes(flag, path, comparsion = comparsion))
    
    def view_file_changes(self):
        self.ui.diff_textBrowser.clear()
        if self.ui.files_listWidget.count():
            commit = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1).text()
            comparsion = None
            if self.ui.repositoryTableWidget.currentRow()+1 != self.ui.repositoryTableWidget.rowCount():
                comparsion = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow()+1, 1).text()
            flag, path = self.ui.files_listWidget.currentItem().text().split(None, 1)
            path = "\ ".join(path.split())
            self.ui.diff_textBrowser.setText(get_unstaged_file_changes(flag, path, commit, comparsion))

    def move_files(fwidget, twidget):
        selected = []
        for item in fwidget.selectedItems():
            selected.append(item.text().split()[1])
            QListWidgetItem(item.text(), twidget)
            fwidget.takeItem(fwidget.row(item))
        return selected

    def stage_files(self):
        if len(self.ui.Unstaged_listwidget.selectedItems()) > 0:
            for item in self.ui.Unstaged_listwidget.selectedItems():
                splited_item = item.text().split()
                if splited_item[0] == 'D':
                    git_rm(splited_item[1])
                else:
                    git_add(splited_item[1])
            self.view_current_changes()
        else:
            QMessageBox.critical(self, "Error", "You must select unstaged file(s) to stage!", QMessageBox.Ok)

    def unstage_files(self):
        if len(self.ui.Staged_listWidget.selectedItems()) > 0:
            selected = []
            for item in self.ui.Staged_listWidget.selectedItems():
                selected.append(item.text().split()[1])
                if self.ui.repositoryTableWidget.rowCount() > 1:
                    git_reset_head(selected)
                else:
                    git_rm_cached(selected)
            self.view_current_changes()
        else:
            QMessageBox.critical(self, "Error", "You must select staged file(s) to unstage!", QMessageBox.Ok)

    def discard_files(self):
        if len(self.ui.Unstaged_listwidget.selectedItems()) > 0:
            reply = QMessageBox.question(self, 'Discard', 'Do you want to discard changes?', QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                for item in self.ui.Unstaged_listwidget.selectedItems():
                    splited_item = item.text().split()
                    if splited_item[0] == '??':
                        clean(splited_item[1])
                    else:
                        git_check_out(splited_item[1])
                self.view_current_changes()
        else:
            QMessageBox.critical(self, "Error", "You must select unstaged file(s) to discard!", QMessageBox.Ok)

    def commit_files(self):
        message = self.ui.commit_lineEdit.text()
        if message == "":
            QMessageBox.critical(self, "Error", "You must write some commit message!", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Commit", commit(message), QMessageBox.Ok)
            self.view_repository()
            self.ui.commit_lineEdit.clear()

    def cherry_pick_menu(self, position):
        if self.ui.repositoryTableWidget.currentRow() > 0:
            menu = QMenu()
            cherry_pick_action = menu.addAction('Cherry pick') 
            QObject.connect(cherry_pick_action, SIGNAL('triggered()'), self.cherry_pick)
            menu.exec_(self.ui.repositoryTableWidget.mapToGlobal(position))

    def cherry_pick(self):
        self.cpdw = CherryPickDialogWrapper(self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1).text(), self)
        self.cpdw.exec_()

    def stash(self):
        QMessageBox.information(self, "Stash", stash(), QMessageBox.Ok)
        self.view_repository()

    def stashes(self):
        sdw = StashesDialogWrapper(self)
        sdw.exec_()
        QObject.connect(sdw, SIGNAL('accepted()'), self.view_repository)
