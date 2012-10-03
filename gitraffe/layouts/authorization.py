# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created: Thu Sep 27 18:45:26 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName(_fromUtf8("Authorization"))
        Authorization.resize(253, 161)
        Authorization.setMinimumSize(QtCore.QSize(253, 161))
        Authorization.setMaximumSize(QtCore.QSize(253, 161))
        self.buttonBox = QtGui.QDialogButtonBox(Authorization)
        self.buttonBox.setGeometry(QtCore.QRect(-110, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(Authorization)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 211, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.Username_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Username_lineEdit.setObjectName(_fromUtf8("Username_lineEdit"))
        self.verticalLayout.addWidget(self.Username_lineEdit)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.Password_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Password_lineEdit.setObjectName(_fromUtf8("Password_lineEdit"))
        self.verticalLayout.addWidget(self.Password_lineEdit)

        self.retranslateUi(Authorization)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Authorization.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Authorization.reject)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QtGui.QApplication.translate("Authorization", "Authorization", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Authorization", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Authorization", "Password:", None, QtGui.QApplication.UnicodeUTF8))

