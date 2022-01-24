# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Init_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 325)
        MainWindow.setFixedSize(710, 325)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 701, 321))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.centralLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setObjectName("centralLayout")
        self.buttonWidget = QtWidgets.QWidget(self.gridLayoutWidget_4)
        self.buttonWidget.setEnabled(True)
        self.buttonWidget.setObjectName("buttonWidget")
        self.buttonWidget.setStyleSheet('''
            QWidget#buttonWidget{
                background-color:rgb(6, 31, 62);
                }
            QPushButton{
                border:none;
                font-size: 15px;
                color:white;
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;}
                QPushButton:hover{
                background-color:rgb(20,170,200);
                }
                ''')
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.buttonWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 171, 261))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.buttonLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.signupBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.signupBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.signupBtn.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("RecordItem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signupBtn.setIcon(icon)
        self.signupBtn.setObjectName("signupBtn")
        self.buttonLayout.addWidget(self.signupBtn, 2, 0, 1, 1)
        self.blueToothBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.blueToothBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.blueToothBtn.setAutoFillBackground(True)
        self.blueToothBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bluetooth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blueToothBtn.setIcon(icon1)
        self.blueToothBtn.setObjectName("blueToothBtn")
        self.buttonLayout.addWidget(self.blueToothBtn, 0, 0, 1, 1)
        self.databaseConnBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.databaseConnBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.databaseConnBtn.setAutoFillBackground(True)
        self.databaseConnBtn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Dataview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.databaseConnBtn.setIcon(icon2)
        self.databaseConnBtn.setObjectName("databaseConnBtn")
        self.buttonLayout.addWidget(self.databaseConnBtn, 1, 0, 1, 1)
        self.writeBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.writeBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.writeBtn.setAutoFillBackground(True)
        self.writeBtn.setIcon(icon)
        self.writeBtn.setObjectName("writeBtn")
        self.buttonLayout.addWidget(self.writeBtn, 3, 0, 1, 1)
        self.centralLayout.addWidget(self.buttonWidget, 0, 0, 1, 1)
        self.infoWidget = QtWidgets.QWidget(self.gridLayoutWidget_4)
        self.infoWidget.setObjectName("infoWidget")
        self.infoWidget.setStyleSheet('''
            QWidget#infoWidget{ 
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                 ''')
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.infoWidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 521, 401))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.infoLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.searchWidget = QtWidgets.QWidget(self.gridLayoutWidget_5)
        self.searchWidget.setObjectName("searchWidget")
        self.searchWidget.setStyleSheet('''
            QWidget#searchWidget{ 
                background-color:white;
                border:none;
                 ''')
        self.gridLayoutWidget = QtWidgets.QWidget(self.searchWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 461, 27))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.searchLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.searchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLayout.setObjectName("searchLayout")
        self.searchTxt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.searchTxt.setMinimumSize(QtCore.QSize(0, 20))
        self.searchTxt.setObjectName("searchTxt")
        self.searchTxt.setStyleSheet('''
            QLineEdit{ 
                border:1px solid gray;
                width:300px;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                padding:2px 4px;}
                 ''')
        self.searchLayout.addWidget(self.searchTxt, 0, 1, 1, 1)
        self.searchBtnwidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.searchBtnwidget.setObjectName("searchBtnwidget")
        self.searchBtnwidget.setStyleSheet('''
            QWidget#searchBtnwidget{ 
                background-color:rgb(6, 31, 62);
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;}
            QWidget#searchBtnwidget:hover{ 
                background-color:rgb(250,250,150)}
            QPushButton#searchBtn{
                border:none;
            }
                 ''')

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.searchBtnwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 81, 22))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.searchBtnLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.searchBtnLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBtnLayout.setObjectName("searchBtnLayout")
        self.searchBtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.searchBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.searchBtn.setAutoFillBackground(False)
        self.searchBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon3)
        self.searchBtn.setObjectName("searchBtn")
        self.searchBtnLayout.addWidget(self.searchBtn, 0, 0, 1, 1)
        self.searchLayout.addWidget(self.searchBtnwidget, 0, 0, 1, 1)
        self.searchLayout.setColumnStretch(0, 1)
        self.searchLayout.setColumnStretch(1, 5)
        self.infoLayout.addWidget(self.searchWidget, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QWidget(self.gridLayoutWidget_5)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tableWidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 521, 261))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.tableLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.tableLayout.setContentsMargins(0, 0, 0, 0)
        self.tableLayout.setObjectName("tableLayout")
        self.infoTable = QtWidgets.QTableView(self.gridLayoutWidget_6)
        self.infoTable.setStyleSheet("border:none;")
        self.infoTable.setDragEnabled(False)
        self.infoTable.setObjectName("infoTable")
        self.tableLayout.addWidget(self.infoTable, 0, 0, 1, 1)
        self.infoLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.infoLayout.setRowStretch(0, 1)
        self.infoLayout.setRowStretch(1, 6)
        self.centralLayout.addWidget(self.infoWidget, 0, 1, 1, 1)
        self.centralLayout.setColumnStretch(0, 1)
        self.centralLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartS Manager"))
        self.signupBtn.setText(_translate("MainWindow", "RECORD ITEM"))
        self.blueToothBtn.setText(_translate("MainWindow", "BLUETOOTH"))
        self.databaseConnBtn.setText(_translate("MainWindow", "ITEM LIST"))
        self.writeBtn.setText(_translate("MainWindow", "INPUT INFO"))
