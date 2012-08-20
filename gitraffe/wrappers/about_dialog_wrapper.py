from PyQt4.QtGui import QDialog
from layouts.about_dialog import Ui_AboutDialog

class AboutDialogWrapper(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
