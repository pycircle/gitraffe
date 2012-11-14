from PyQt4.QtGui import QDialog, QInputDialog, QMessageBox
from PyQt4.QtCore import QObject, SIGNAL
from os.path import exists, expanduser
from layouts.settings_dialog import Ui_SettingsDialog
from wrappers.authorization_wrapper import AuthorizationWrapper
from git.settings import get_settings, set_settings
from ssh import get_ssh_key, backup, generate_new_ssh_key

class SettingsDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.dialog = AuthorizationWrapper(self)
        self.parent = parent
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        settings = get_settings()
        self.ui.usernameEdit.setText(settings[0])
        self.ui.emailEdit.setText(settings[1])
        self.ssh_key()
        QObject.connect(self, SIGNAL('accepted()'), self.update_settings)
        QObject.connect(self.ui.generateButton, SIGNAL('clicked()'), self.check_key_existence)
        QObject.connect(self.dialog, SIGNAL('accepted()'), self.generate)

    def ssh_key(self):
        self.ui.sshTextEdit.setText(get_ssh_key())

    def update_settings(self):
        set_settings(self.ui.usernameEdit.text(), self.ui.emailEdit.text())
    
    def generate(self):
        QMessageBox.information(self, 'Generated new key', generate_new_ssh_key(self.dialog.username, self.dialog.password), QMessageBox.Ok)
        self.ssh_key()

    def ask_for_auth(self):
        self.dialog.ui.label.setText('Email:')
        self.dialog.exec_()
        QObject.connect(self.dialog, SIGNAL('accepted()'), self.generate)

    def check_key_existence(self):
        if exists((expanduser('~/.ssh/id_rsa.pub'))) or exists((expanduser('~/.ssh/id_rsa.pub'))):
            reply = QMessageBox.question(self, 'Existing key', 'Do you want to override the existing SSH key?', QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                backup()
                self.ask_for_auth()
        else:
            self.ask_for_auth()
