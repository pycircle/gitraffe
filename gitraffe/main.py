#!/usr/bin/env python3

import sys
from layouts.main_window_wrapper import MainWindowWrapper, QtGui
import db_adapter

if __name__ == '__main__':
    db_adapter.init()

    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowWrapper()
    main_window.show()
    sys.exit(app.exec_())
