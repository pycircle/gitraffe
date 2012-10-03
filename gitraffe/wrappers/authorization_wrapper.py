from PyQt4.QtGui import QDialog, QLineEdit
from PyQt4.QtCore import QObject, SIGNAL
from layouts.authorization import Ui_Authorization

class AuthorizationWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.ui.Password_lineEdit.setEchoMode(QLineEdit.Password)
        self.username = ""
        self.password = ""
    def accept(self):
        self.username = self.ui.Username_lineEdit.text()
        self.password = self.ui.Password_lineEdit.text()
        QDialog.accept(self)
