from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow

class Wrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 