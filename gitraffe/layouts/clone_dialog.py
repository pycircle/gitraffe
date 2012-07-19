# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_dialog.ui'
#
# Created: Thu Jul 19 15:54:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(436, 183)
        Dialog.setMinimumSize(QtCore.QSize(436, 183))
        Dialog.setMaximumSize(QtCore.QSize(436, 183))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 81))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Source_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.Source_lineEdit.setObjectName(_fromUtf8("Source_lineEdit"))
        self.horizontalLayout.addWidget(self.Source_lineEdit)
        self.Source_push = QtGui.QPushButton(self.layoutWidget)
        self.Source_push.setObjectName(_fromUtf8("Source_push"))
        self.horizontalLayout.addWidget(self.Source_push)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Destination_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.Destination_lineEdit.setObjectName(_fromUtf8("Destination_lineEdit"))
        self.horizontalLayout_2.addWidget(self.Destination_lineEdit)
        self.Destination_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.Destination_pushButton.setObjectName(_fromUtf8("Destination_pushButton"))
        self.horizontalLayout_2.addWidget(self.Destination_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 140, 178, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Clone_button = QtGui.QPushButton(self.layoutWidget1)
        self.Clone_button.setObjectName(_fromUtf8("Clone_button"))
        self.horizontalLayout_3.addWidget(self.Clone_button)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Source:", None, QtGui.QApplication.UnicodeUTF8))
        self.Source_push.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Destination:", None, QtGui.QApplication.UnicodeUTF8))
        self.Destination_pushButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.Clone_button.setText(QtGui.QApplication.translate("Dialog", "Clone", None, QtGui.QApplication.UnicodeUTF8))

