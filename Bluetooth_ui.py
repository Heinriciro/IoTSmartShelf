# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bluetooth_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(318, 458)
        Form.setFixedSize(318, 458)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 301, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.searchWidget.setObjectName("searchWidget")
        self.searchWidget.setStyleSheet('''
            QWidget#searchWidget{
                background-color:white;
                border-radius:10px;
                }
            QWidget#searchWidget:hover{
                color:white;
                background-color:rgb(250, 250, 200);
                }
            QPushButton{
                border:none;
                font-size: 15px;
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;}
                ''')
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.searchWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 42))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.searchLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.searchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLayout.setObjectName("searchLayout")
        self.scanBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.scanBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.scanBtn.setObjectName("scanBtn")
        self.searchLayout.addWidget(self.scanBtn, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.searchWidget, 1, 0, 1, 1)
        self.diconnWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.diconnWidget.setObjectName("diconnWidget")
        self.diconnWidget.setStyleSheet('''
            QWidget#diconnWidget{
                background-color:white;
                border-radius:10px;
                }
            QWidget#diconnWidget:hover{
                color:white;
                background-color:rgb(250, 250, 200);
                }
            QPushButton{
                border:none;
                font-size: 15px;
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;}
                ''')
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.diconnWidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 301, 42))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.disconnLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.disconnLayout.setContentsMargins(0, 0, 0, 0)
        self.disconnLayout.setObjectName("disconnLayout")
        self.disconnBtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.disconnBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.disconnBtn.setObjectName("disconnBtn")
        self.disconnLayout.addWidget(self.disconnBtn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.diconnWidget, 3, 0, 1, 1)
        self.connWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.connWidget.setObjectName("connWidget")
        self.connWidget.setStyleSheet('''
            QWidget#connWidget{
                background-color:white;
                border-radius:10px;
                }
            QWidget#connWidget:hover{
                color:white;
                background-color:rgb(250, 250, 200);
                }
            QPushButton{
                border:none;
                font-size: 15px;
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;}
                ''')

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.connWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 301, 42))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.connLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.connLayout.setContentsMargins(0, 0, 0, 0)
        self.connLayout.setObjectName("connLayout")
        self.connBtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.connBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.connBtn.setObjectName("connBtn")
        self.connLayout.addWidget(self.connBtn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.connWidget, 2, 0, 1, 1)
        self.blueList = QtWidgets.QTableView(self.gridLayoutWidget)
        self.blueList.setObjectName("blueList")
        self.blueList.setAlternatingRowColors(True)
        self.blueList.setStyleSheet('''
            QTableView{
                gridline-color: black;
                background-color: rgb(250,250,250);
                alternate-background-color: rgb(250,250,150);
                border:none;
            }
            QTableView:item{
                selection-background-color: rgb(60,100,40);
            }
            QTableView QHeaderView:section{
                background-color: rgb(6, 31, 62);
                color:white;
                font:bold 10pt "微软雅黑";
                border-bottom:1px solid black;
            }

        ''')
        self.blueList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.blueList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.gridLayout.addWidget(self.blueList, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 8)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BLUETOOTH"))
        self.scanBtn.setText(_translate("Form", "SEARCH FOR THE BLUETOOTH"))
        self.disconnBtn.setText(_translate("Form", "DISCONNECT"))
        self.connBtn.setText(_translate("Form", "CONNECT"))
