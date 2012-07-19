from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog, QIcon, QTableWidgetItem
from PyQt4.QtCore import QDir, QObject, SIGNAL, Qt
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git import check_repository, open_repository, get_graph
import db_adapter
import os
from layouts import main_window
from layouts.clone_dialog_wrapper import CloneWindowWrapper
#from structures import Repository

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Repository list
        self.ui.listWidget.setMouseTracking(True)
        self.ui.listWidget.itemClicked.connect(self.view_repository)
        self.list_all_repositories()
        # Menu/toolbar
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
        QObject.connect(self.ui.actionDelete_repository, SIGNAL('triggered()'), self.delete_listWidgetitem)
        QObject.connect(self.ui.actionClone_repository_3, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository_2, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository, SIGNAL('triggered()'), self.clone_respoitory)

    def list_all_repositories(self):
        repositories = db_adapter.get_repositories()
        for repository in repositories:
            repo = QListWidgetItem(QIcon(os.path.dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), repository.name, self.ui.listWidget)
            repo.setStatusTip(repository.path)
            repo.setFlags(repo.flags() | Qt.ItemIsEditable)

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="":
            path = check_repository(directory)
            if path[0]:
                directory = path[1]
                name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(directory))
                if name[1]:
                    self.add_to_list(name[0], directory)
            else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)

    def add_to_list(self, name, directory):
        db_adapter.add_repository(name, directory)
        repo = QListWidgetItem(QIcon(os.path.dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), name, self.ui.listWidget)
        repo.setStatusTip(directory)
        repo.setFlags(repo.flags() | Qt.ItemIsEditable)

    def delete_listWidgetitem(self):
        if self.ui.listWidget.count()!=0:
            respond = QMessageBox.question(self, "Delete", 
                                           "Are you sure, that you want delete " + self.ui.listWidget.item(self.ui.listWidget.currentRow()).text(),
                                           QMessageBox.Ok, QMessageBox.Cancel)
            if respond==QMessageBox.Ok:
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def graph(self):
        i = 0
        graph = get_graph()
        self.ui.repositoryTableWidget.setRowCount(len(graph))
        for row in graph:
            j = 0
            for col in row:
                item = QTableWidgetItem(col)
                self.ui.repositoryTableWidget.setItem(i, j, item)
                j += 1
            i += 1

    def view_repository(self):
        name = self.ui.listWidget.item(self.ui.listWidget.currentRow()).text()
        repository = db_adapter.get_repository_by_name(name)
        open_repository(repository.path)
#        print(get_graph())
        self.graph()

    def clone_respoitory(self):
        cwd = CloneWindowWrapper(self)
        cwd.exec_()
