import sys
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    main_window_ui = Ui_MainWindow()
    main_window_ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())