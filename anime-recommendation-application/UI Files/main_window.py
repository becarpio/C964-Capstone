# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_txtinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.main_txtinput.setObjectName("main_txtinput")
        self.horizontalLayout.addWidget(self.main_txtinput)
        self.main_btn_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_filter.setObjectName("main_btn_filter")
        self.horizontalLayout.addWidget(self.main_btn_filter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.main_listview_animetitles = QtWidgets.QListView(self.verticalLayoutWidget)
        self.main_listview_animetitles.setObjectName("main_listview_animetitles")
        self.verticalLayout_2.addWidget(self.main_listview_animetitles)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_btn_graph1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_graph1.setObjectName("main_btn_graph1")
        self.horizontalLayout_3.addWidget(self.main_btn_graph1)
        self.main_btn_graph2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_graph2.setObjectName("main_btn_graph2")
        self.horizontalLayout_3.addWidget(self.main_btn_graph2)
        self.main_btn_graph3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_graph3.setObjectName("main_btn_graph3")
        self.horizontalLayout_3.addWidget(self.main_btn_graph3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_btn_reccomend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_reccomend.setObjectName("main_btn_reccomend")
        self.horizontalLayout_2.addWidget(self.main_btn_reccomend)
        self.main_btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_exit.setObjectName("main_btn_exit")
        self.horizontalLayout_2.addWidget(self.main_btn_exit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime Recommendations"))
        self.main_txtinput.setText(_translate("MainWindow", "Enter Anime Title"))
        self.main_btn_filter.setText(_translate("MainWindow", "Filter"))
        self.main_btn_graph1.setText(_translate("MainWindow", "Correlation Matrix"))
        self.main_btn_graph2.setText(_translate("MainWindow", "Undecided Report 2"))
        self.main_btn_graph3.setText(_translate("MainWindow", "Undecided Report 3"))
        self.main_btn_reccomend.setText(_translate("MainWindow", "Recommendations"))
        self.main_btn_exit.setText(_translate("MainWindow", "Exit"))

