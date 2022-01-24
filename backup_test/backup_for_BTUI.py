# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bluetooth_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(304, 393)
        Form.setFixedSize(304, 393)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 301, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.connLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.connLayout.setContentsMargins(0, 0, 0, 0)
        self.connLayout.setObjectName("connLayout")
        self.connBtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.connBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.connBtn.setObjectName("connBtn")
        self.connLayout.addWidget(self.connBtn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.connWidget, 2, 0, 1, 1)
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.searchLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.searchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLayout.setObjectName("searchLayout")
        self.scanBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.scanBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.scanBtn.setObjectName("scanBtn")
        self.searchLayout.addWidget(self.scanBtn, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.searchWidget, 1, 0, 1, 1)
        self.blueList = QtWidgets.QTableView(self.gridLayoutWidget)
        self.blueList.setObjectName("blueList")
        self.blueList.setStyleSheet("border:none;")
        self.blueList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.blueList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.gridLayout.addWidget(self.blueList, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.connBtn.setText(_translate("Form", "CONNECT"))
        self.scanBtn.setText(_translate("Form", "SEARCH FOR THE BLUETOOTH"))
