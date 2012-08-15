# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created: Wed Aug 15 11:13:52 2012
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
        self.verticalLayout = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.userdataTab = QtGui.QWidget()
        self.userdataTab.setObjectName(_fromUtf8("userdataTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.userdataTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.settingsLayout = QtGui.QVBoxLayout()
        self.settingsLayout.setObjectName(_fromUtf8("settingsLayout"))
        self.usernameLayout = QtGui.QHBoxLayout()
        self.usernameLayout.setObjectName(_fromUtf8("usernameLayout"))
        self.usernameLabel = QtGui.QLabel(self.userdataTab)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.usernameLayout.addWidget(self.usernameLabel)
        self.usernameEdit = QtGui.QLineEdit(self.userdataTab)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.usernameLayout.addWidget(self.usernameEdit)
        self.settingsLayout.addLayout(self.usernameLayout)
        self.emailLayout = QtGui.QHBoxLayout()
        self.emailLayout.setObjectName(_fromUtf8("emailLayout"))
        self.emailLabel = QtGui.QLabel(self.userdataTab)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.emailLayout.addWidget(self.emailLabel)
        self.emailEdit = QtGui.QLineEdit(self.userdataTab)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.emailLayout.addWidget(self.emailEdit)
        self.settingsLayout.addLayout(self.emailLayout)
        self.verticalLayout_2.addLayout(self.settingsLayout)
        self.tabWidget.addTab(self.userdataTab, _fromUtf8(""))
        self.sshTab = QtGui.QWidget()
        self.sshTab.setObjectName(_fromUtf8("sshTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.sshTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.sshTextEdit = QtGui.QTextEdit(self.sshTab)
        self.sshTextEdit.setReadOnly(True)
        self.sshTextEdit.setObjectName(_fromUtf8("sshTextEdit"))
        self.verticalLayout_3.addWidget(self.sshTextEdit)
        self.tabWidget.addTab(self.sshTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Email:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userdataTab), QtGui.QApplication.translate("SettingsDialog", "User data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sshTab), QtGui.QApplication.translate("SettingsDialog", "SSH key", None, QtGui.QApplication.UnicodeUTF8))

