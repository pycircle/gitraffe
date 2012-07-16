from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog, QIcon
from PyQt4.QtCore import QDir, QObject, SIGNAL, Qt
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git import check_repository
import os
from layouts import main_window

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.setMouseTracking(True)
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
        QObject.connect(self.ui.actionDelete_repository, SIGNAL('triggered()'), self.delete_listWidgetitem)
    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        path = check_repository(directory)
        if directory!="" and path[0]:
            directory = path[1]
            name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(directory))
            if name[1]:
                repo = QListWidgetItem(QIcon(os.path.dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), name[0], self.ui.listWidget)
                repo.setStatusTip(directory)
                repo.setFlags(repo.flags() | Qt.ItemIsEditable)
        elif directory=="": pass
        else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)
    def delete_listWidgetitem(self):
        if self.ui.listWidget.count()!=0:
            respond = QMessageBox.question(self, "Delete", 
                                           "Are you sure, that you want delete " + self.ui.listWidget.item(self.ui.listWidget.currentRow()).text(),
                                           QMessageBox.Ok, QMessageBox.Cancel)
            if respond==QMessageBox.Ok:
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    
    