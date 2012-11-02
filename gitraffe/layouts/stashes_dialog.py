# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stashes_dialog.ui'
#
# Created: Fri Nov  2 20:11:47 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StashesDialog(object):
    def setupUi(self, StashesDialog):
        StashesDialog.setObjectName(_fromUtf8("StashesDialog"))
        StashesDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(StashesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stashesListWidget = QtGui.QListWidget(StashesDialog)
        self.stashesListWidget.setObjectName(_fromUtf8("stashesListWidget"))
        self.verticalLayout.addWidget(self.stashesListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.applyButton = QtGui.QPushButton(StashesDialog)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout.addWidget(self.applyButton)
        self.dropButton = QtGui.QPushButton(StashesDialog)
        self.dropButton.setObjectName(_fromUtf8("dropButton"))
        self.horizontalLayout.addWidget(self.dropButton)
        self.buttonBox = QtGui.QDialogButtonBox(StashesDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(StashesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StashesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StashesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StashesDialog)

    def retranslateUi(self, StashesDialog):
        StashesDialog.setWindowTitle(QtGui.QApplication.translate("StashesDialog", "Stashes", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("StashesDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.dropButton.setText(QtGui.QApplication.translate("StashesDialog", "Drop", None, QtGui.QApplication.UnicodeUTF8))

