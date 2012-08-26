#!/usr/bin/env python3.2

import sys
import os

config_dir = '~/.gitraffe'

if __name__ == '__main__':
    if not os.path.exists(os.path.expanduser(config_dir)):
        os.mkdir(os.path.expanduser(config_dir))

    from wrappers.main_window_wrapper import MainWindowWrapper, QtGui
    import db_adapter
    from log import clear_log

    db_adapter.init()
    clear_log()

    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowWrapper()
    main_window.show()
    sys.exit(app.exec_())
