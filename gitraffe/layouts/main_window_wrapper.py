from PyQt4.QtGui import QMainWindow, QFileDialog, qApp
from PyQt4.QtCore import QDir, QObject, SIGNAL
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
#from structures import Repositories_table


class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="":
            #===================================================================
            # model = Repositories_table(0, 'first', directory, self)
            # self.ui.repositoriesListView(model)
            #===================================================================