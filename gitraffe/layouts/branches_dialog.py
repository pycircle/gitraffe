# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branches_dialog.ui'
#
# Created: Fri Aug  3 19:11:00 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BranchesDialog(object):
    def setupUi(self, BranchesDialog):
        BranchesDialog.setObjectName(_fromUtf8("BranchesDialog"))
        BranchesDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(BranchesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.branchesTabWidget = QtGui.QTabWidget(BranchesDialog)
        self.branchesTabWidget.setObjectName(_fromUtf8("branchesTabWidget"))
        self.localTab = QtGui.QWidget()
        self.localTab.setObjectName(_fromUtf8("localTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.localTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.localBranchesListWidget = QtGui.QListWidget(self.localTab)
        self.localBranchesListWidget.setObjectName(_fromUtf8("localBranchesListWidget"))
        self.verticalLayout_2.addWidget(self.localBranchesListWidget)
        self.branchesTabWidget.addTab(self.localTab, _fromUtf8(""))
        self.remoteTab = QtGui.QWidget()
        self.remoteTab.setObjectName(_fromUtf8("remoteTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.remoteTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.remoteBranchesListWidget = QtGui.QListWidget(self.remoteTab)
        self.remoteBranchesListWidget.setObjectName(_fromUtf8("remoteBranchesListWidget"))
        self.verticalLayout_3.addWidget(self.remoteBranchesListWidget)
        self.branchesTabWidget.addTab(self.remoteTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.branchesTabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(BranchesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BranchesDialog)
        self.branchesTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BranchesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BranchesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BranchesDialog)

    def retranslateUi(self, BranchesDialog):
        BranchesDialog.setWindowTitle(QtGui.QApplication.translate("BranchesDialog", "Change branch", None, QtGui.QApplication.UnicodeUTF8))
        self.branchesTabWidget.setTabText(self.branchesTabWidget.indexOf(self.localTab), QtGui.QApplication.translate("BranchesDialog", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.branchesTabWidget.setTabText(self.branchesTabWidget.indexOf(self.remoteTab), QtGui.QApplication.translate("BranchesDialog", "Remote", None, QtGui.QApplication.UnicodeUTF8))

