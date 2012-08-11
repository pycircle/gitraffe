# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created: Fri Aug 10 18:10:12 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(400, 200)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.settingsLayout = QtGui.QVBoxLayout()
        self.settingsLayout.setObjectName(_fromUtf8("settingsLayout"))
        self.usernameLayout = QtGui.QHBoxLayout()
        self.usernameLayout.setObjectName(_fromUtf8("usernameLayout"))
        self.usernameLabel = QtGui.QLabel(SettingsDialog)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.usernameLayout.addWidget(self.usernameLabel)
        self.usernameEdit = QtGui.QLineEdit(SettingsDialog)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.usernameLayout.addWidget(self.usernameEdit)
        self.settingsLayout.addLayout(self.usernameLayout)
        self.emailLayout = QtGui.QHBoxLayout()
        self.emailLayout.setObjectName(_fromUtf8("emailLayout"))
        self.emailLabel = QtGui.QLabel(SettingsDialog)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.emailLayout.addWidget(self.emailLabel)
        self.emailEdit = QtGui.QLineEdit(SettingsDialog)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.emailLayout.addWidget(self.emailEdit)
        self.settingsLayout.addLayout(self.emailLayout)
        self.verticalLayout_2.addLayout(self.settingsLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Email:", None, QtGui.QApplication.UnicodeUTF8))

