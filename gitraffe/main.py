import sys
from layouts.wrapper import Wrapper, QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = Wrapper()
    main_window.show()
    sys.exit(app.exec_())