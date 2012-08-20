from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QObject, SIGNAL
from layouts.settings_dialog import Ui_SettingsDialog
from git import get_settings, set_settings, get_ssh_key

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

    def update_settings(self):
        set_settings(self.ui.usernameEdit.text(), self.ui.emailEdit.text())
