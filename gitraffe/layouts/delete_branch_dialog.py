# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_branch_dialog.ui'
#
# Created: Sun Aug  5 21:13:04 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteBranchDialog(object):
    def setupUi(self, DeleteBranchDialog):
        DeleteBranchDialog.setObjectName(_fromUtf8("DeleteBranchDialog"))
        DeleteBranchDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DeleteBranchDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.branches2delListWidget = QtGui.QListWidget(DeleteBranchDialog)
        self.branches2delListWidget.setObjectName(_fromUtf8("branches2delListWidget"))
        self.verticalLayout.addWidget(self.branches2delListWidget)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteBranchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DeleteBranchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DeleteBranchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DeleteBranchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteBranchDialog)

    def retranslateUi(self, DeleteBranchDialog):
        DeleteBranchDialog.setWindowTitle(QtGui.QApplication.translate("DeleteBranchDialog", "Delete branch", None, QtGui.QApplication.UnicodeUTF8))

