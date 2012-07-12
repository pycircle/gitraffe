# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Jul 12 20:14:43 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 525)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.repositoriesListView = QtGui.QListView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repositoriesListView.sizePolicy().hasHeightForWidth())
        self.repositoriesListView.setSizePolicy(sizePolicy)
        self.repositoriesListView.setObjectName(_fromUtf8("repositoriesListView"))
        self.horizontalLayout_2.addWidget(self.repositoriesListView)
        self.repositoryLayout = QtGui.QVBoxLayout()
        self.repositoryLayout.setObjectName(_fromUtf8("repositoryLayout"))
        self.treeColumnView = QtGui.QColumnView(self.centralwidget)
        self.treeColumnView.setObjectName(_fromUtf8("treeColumnView"))
        self.repositoryLayout.addWidget(self.treeColumnView)
        self.changesetLayout = QtGui.QHBoxLayout()
        self.changesetLayout.setObjectName(_fromUtf8("changesetLayout"))
        self.changesetButtonsLayout = QtGui.QVBoxLayout()
        self.changesetButtonsLayout.setObjectName(_fromUtf8("changesetButtonsLayout"))
        self.stageButton = QtGui.QPushButton(self.centralwidget)
        self.stageButton.setObjectName(_fromUtf8("stageButton"))
        self.changesetButtonsLayout.addWidget(self.stageButton)
        self.unstageButton = QtGui.QPushButton(self.centralwidget)
        self.unstageButton.setObjectName(_fromUtf8("unstageButton"))
        self.changesetButtonsLayout.addWidget(self.unstageButton)
        self.separator = QtGui.QFrame(self.centralwidget)
        self.separator.setFrameShape(QtGui.QFrame.HLine)
        self.separator.setFrameShadow(QtGui.QFrame.Sunken)
        self.separator.setObjectName(_fromUtf8("separator"))
        self.changesetButtonsLayout.addWidget(self.separator)
        self.pullButton = QtGui.QPushButton(self.centralwidget)
        self.pullButton.setObjectName(_fromUtf8("pullButton"))
        self.changesetButtonsLayout.addWidget(self.pullButton)
        self.commitButton = QtGui.QPushButton(self.centralwidget)
        self.commitButton.setObjectName(_fromUtf8("commitButton"))
        self.changesetButtonsLayout.addWidget(self.commitButton)
        self.stashButton = QtGui.QPushButton(self.centralwidget)
        self.stashButton.setObjectName(_fromUtf8("stashButton"))
        self.changesetButtonsLayout.addWidget(self.stashButton)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.changesetButtonsLayout.addWidget(self.pushButton)
        self.changesetLayout.addLayout(self.changesetButtonsLayout)
        self.filesListView = QtGui.QListView(self.centralwidget)
        self.filesListView.setObjectName(_fromUtf8("filesListView"))
        self.changesetLayout.addWidget(self.filesListView)
        self.diffTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.diffTextEdit.setObjectName(_fromUtf8("diffTextEdit"))
        self.changesetLayout.addWidget(self.diffTextEdit)
        self.repositoryLayout.addLayout(self.changesetLayout)
        self.horizontalLayout_2.addLayout(self.repositoryLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuRepository = QtGui.QMenu(self.menubar)
        self.menuRepository.setObjectName(_fromUtf8("menuRepository"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClone_repository = QtGui.QAction(MainWindow)
        self.actionClone_repository.setObjectName(_fromUtf8("actionClone_repository"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionAbout_PyGitGui = QtGui.QAction(MainWindow)
        self.actionAbout_PyGitGui.setObjectName(_fromUtf8("actionAbout_PyGitGui"))
        self.actionPull = QtGui.QAction(MainWindow)
        self.actionPull.setObjectName(_fromUtf8("actionPull"))
        self.actionAdd_files = QtGui.QAction(MainWindow)
        self.actionAdd_files.setObjectName(_fromUtf8("actionAdd_files"))
        self.actionRemove_files = QtGui.QAction(MainWindow)
        self.actionRemove_files.setObjectName(_fromUtf8("actionRemove_files"))
        self.actionCommit = QtGui.QAction(MainWindow)
        self.actionCommit.setObjectName(_fromUtf8("actionCommit"))
        self.actionPush = QtGui.QAction(MainWindow)
        self.actionPush.setObjectName(_fromUtf8("actionPush"))
        self.actionChange_branch = QtGui.QAction(MainWindow)
        self.actionChange_branch.setObjectName(_fromUtf8("actionChange_branch"))
        self.actionCherry_pick = QtGui.QAction(MainWindow)
        self.actionCherry_pick.setObjectName(_fromUtf8("actionCherry_pick"))
        self.actionClone_repository_2 = QtGui.QAction(MainWindow)
        self.actionClone_repository_2.setObjectName(_fromUtf8("actionClone_repository_2"))
        self.actionAdd_existing_repository = QtGui.QAction(MainWindow)
        self.actionAdd_existing_repository.setObjectName(_fromUtf8("actionAdd_existing_repository"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout_Gitraffe = QtGui.QAction(MainWindow)
        self.actionAbout_Gitraffe.setObjectName(_fromUtf8("actionAbout_Gitraffe"))
        self.actionClone_repository_3 = QtGui.QAction(MainWindow)
        self.actionClone_repository_3.setObjectName(_fromUtf8("actionClone_repository_3"))
        self.actionAdd_existing_repository_2 = QtGui.QAction(MainWindow)
        self.actionAdd_existing_repository_2.setObjectName(_fromUtf8("actionAdd_existing_repository_2"))
        self.actionStash = QtGui.QAction(MainWindow)
        self.actionStash.setObjectName(_fromUtf8("actionStash"))
        self.menuFile.addAction(self.actionClone_repository_2)
        self.menuFile.addAction(self.actionAdd_existing_repository)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionRefresh)
        self.menuRepository.addAction(self.actionPull)
        self.menuRepository.addAction(self.actionCommit)
        self.menuRepository.addAction(self.actionStash)
        self.menuRepository.addAction(self.actionPush)
        self.menuRepository.addSeparator()
        self.menuRepository.addAction(self.actionChange_branch)
        self.menuRepository.addAction(self.actionCherry_pick)
        self.menuHelp.addAction(self.actionAbout_Gitraffe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRepository.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionClone_repository_3)
        self.toolBar.addAction(self.actionAdd_existing_repository_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        self.stageButton.setText(QtGui.QApplication.translate("MainWindow", "Stage", None, QtGui.QApplication.UnicodeUTF8))
        self.unstageButton.setText(QtGui.QApplication.translate("MainWindow", "Unstage", None, QtGui.QApplication.UnicodeUTF8))
        self.pullButton.setText(QtGui.QApplication.translate("MainWindow", "Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.commitButton.setText(QtGui.QApplication.translate("MainWindow", " Commit", None, QtGui.QApplication.UnicodeUTF8))
        self.stashButton.setText(QtGui.QApplication.translate("MainWindow", "Stash", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Push", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRepository.setTitle(QtGui.QApplication.translate("MainWindow", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_PyGitGui.setText(QtGui.QApplication.translate("MainWindow", "About PyGitGui", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPull.setText(QtGui.QApplication.translate("MainWindow", "Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_files.setText(QtGui.QApplication.translate("MainWindow", "Add files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_files.setText(QtGui.QApplication.translate("MainWindow", "Remove files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommit.setText(QtGui.QApplication.translate("MainWindow", "Commit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPush.setText(QtGui.QApplication.translate("MainWindow", "Push", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange_branch.setText(QtGui.QApplication.translate("MainWindow", "Change branch", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCherry_pick.setText(QtGui.QApplication.translate("MainWindow", "Cherry-pick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository_2.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_existing_repository.setText(QtGui.QApplication.translate("MainWindow", "Add existing repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Gitraffe.setText(QtGui.QApplication.translate("MainWindow", "About Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository_3.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_existing_repository_2.setText(QtGui.QApplication.translate("MainWindow", "Add existing repository", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStash.setText(QtGui.QApplication.translate("MainWindow", "Stash", None, QtGui.QApplication.UnicodeUTF8))
