from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox, QInputDialog
from PyQt4.QtCore import QObject, SIGNAL, QDir
from layouts.clone_dialog import Ui_Clone
from git import check_repository, clone_repository

class CloneWindowWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_Clone()
        self.ui.setupUi(self)
        QObject.connect(self.ui.Clone_button, SIGNAL('clicked()'), self.clone)
        QObject.connect(self.ui.Source_push, SIGNAL('clicked()'), self.s_browse)
        QObject.connect(self.ui.Destination_pushButton, SIGNAL('clicked()'), self.d_browse)

    def clone(self):
        source = self.ui.Source_lineEdit.text()
        destination = self.ui.Destination_lineEdit.text()
        info = clone_repository(source, destination)
        if info[0]:
            name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(destination))
            if name[1]:
                self.parent.add_to_list(name[0], destination)
            self.close()
        elif source == "" or destination == "":  QMessageBox.critical(self, "Error", "There must be destination and source!", QMessageBox.Ok)
        else: QMessageBox.critical(self, "Error", info[1], QMessageBox.Ok)

    def s_browse(self):
        directory = QFileDialog.getExistingDirectory(self,QDir.homePath(), QDir.homePath())
        if directory!="":
            path = check_repository(directory)
            if path[0]:
                self.ui.Source_lineEdit.clear()
                self.ui.Source_lineEdit.insert(directory)
            else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)

    def d_browse(self):
        directory = QFileDialog.getExistingDirectory(self,QDir.homePath(), QDir.homePath())
        if directory!="":
            self.ui.Destination_lineEdit.clear()
            self.ui.Destination_lineEdit.insert(directory)

