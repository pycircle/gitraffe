# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created: Sat Aug  4 17:54:17 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(500, 300)
        self.verticalLayout_3 = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(167, 200))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/about_logo.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.titleLabel = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.descriptionLabel = QtGui.QLabel(AboutDialog)
        self.descriptionLabel.setTextFormat(QtCore.Qt.RichText)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.verticalLayout_2.addWidget(self.descriptionLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("AboutDialog", "Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p>Version 0.1 unstable</p><p><br/></p><p>Gitraffe is a graphical frontend for Git (a revision control system), based on Python, PyQt and Sqlite.</p><p>Licensed under the <a href=\"http://www.gnu.org/copyleft/gpl.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU General Public License version 3</span></a>.</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

