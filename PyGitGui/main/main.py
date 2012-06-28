import sys
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMessageBox()
    w.setText("HAHAHA")
    w.show()
    sys.exit(app.exec_())