from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog
from PyQt4.QtCore import QDir, QObject, SIGNAL
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git import check_repository
import os

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.setMouseTracking(True)
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="" and check_repository(directory):
            directory = check_repository(directory)
            name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(directory))
            if name[1]:
                repo = QListWidgetItem(name[0], self.ui.listWidget)
                repo.setStatusTip(directory)
        else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)