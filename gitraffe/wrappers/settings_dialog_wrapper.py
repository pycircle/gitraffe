from PyQt4.QtGui import QDialog, QInputDialog
from PyQt4.QtCore import QObject, SIGNAL
from layouts.settings_dialog import Ui_SettingsDialog
from git import get_settings, set_settings
from ssh import get_ssh_key, generate_new_ssh_key

class SettingsDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        settings = get_settings()
        self.ui.usernameEdit.setText(settings[0])
        self.ui.emailEdit.setText(settings[1])
        self.ui.sshTextEdit.setText(get_ssh_key())
        QObject.connect(self, SIGNAL('accepted()'), self.update_settings)
        QObject.connect(self.ui.generateButton, SIGNAL('clicked()'), self.generate)

    def update_settings(self):
        set_settings(self.ui.usernameEdit.text(), self.ui.emailEdit.text())

    def generate(self):
        email = QInputDialog().getText(self, 'Email', 'Input your email:')
        if email[1]:
            QMessageBox.information(self, "Generate new key", generate_new_ssh_key(email[0]), QMessageBox.Ok)
