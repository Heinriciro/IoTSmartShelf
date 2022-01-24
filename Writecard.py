# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Writecard.ui'
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
        Form.resize(435, 129)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 411, 111))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.centralLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setObjectName("centralLayout")
        self.weightWidget = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.weightWidget.setObjectName("weightWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.weightWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 0, 331, 27))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.weightLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.weightLayout.setContentsMargins(0, 0, 0, 0)
        self.weightLayout.setObjectName("weightLayout")
        self.weightTxt = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.weightTxt.setMinimumSize(QtCore.QSize(0, 25))
        self.weightTxt.setObjectName("weightTxt")
        self.weightTxt.setStyleSheet('''
            QLineEdit{ 
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;}
                 ''')
        self.weightLayout.addWidget(self.weightTxt, 0, 2, 1, 1)
        self.weightLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.weightLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.weightLabel.setObjectName("weightLabel")
        self.weightLabel.setStyleSheet('''
            QWidget#weightLabel{
            font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;
            font-size:12px;}
        ''')
        self.weightLayout.addWidget(self.weightLabel, 0, 1, 1, 1)
        self.centralLayout.addWidget(self.weightWidget, 1, 0, 1, 1)
        self.DesWidget = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.DesWidget.setObjectName("DesWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.DesWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 361, 27))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.DesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.DesLayout.setContentsMargins(0, 0, 0, 0)
        self.DesLayout.setObjectName("DesLayout")
        self.descLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.descLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.descLabel.setObjectName("descLabel")
        self.descLabel.setStyleSheet('''
            QWidget#descLabel{
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;
                font-size: 12px;
                }
                ''')
        self.DesLayout.addWidget(self.descLabel, 0, 0, 1, 1)
        self.descTxt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.descTxt.setMinimumSize(QtCore.QSize(25, 25))
        self.descTxt.setObjectName("descTxt")
        self.descTxt.setStyleSheet('''
            QLineEdit{ 
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;}
                 ''')
        self.DesLayout.addWidget(self.descTxt, 0, 1, 1, 2)
        self.DesLayout.setColumnStretch(0, 1)
        self.DesLayout.setColumnStretch(1, 10)
        self.centralLayout.addWidget(self.DesWidget, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget_3)
        self.widget.setObjectName("widget")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(140, 10, 121, 25))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.BtnWidget = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.BtnWidget.setContentsMargins(0, 0, 0, 0)
        self.BtnWidget.setObjectName("BtnWidget")
        self.widget.setStyleSheet('''
            QWidget#widget{
                background-color:white;
                border-radius:10px;
                border-radius:10px;
                }
            QWidget#widget:hover{
                color:white;
                background-color:rgb(250, 250, 200);
                }
            QPushButton{
                border:none;
                font-size: 15px;
                font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;}
                ''')
        self.submitBtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.submitBtn.setObjectName("submitBtn")
        self.BtnWidget.addWidget(self.submitBtn, 0, 0, 1, 1)
        self.centralLayout.addWidget(self.widget, 2, 0, 1, 1)
        self.centralLayout.setRowStretch(0, 3)
        self.centralLayout.setRowStretch(1, 3)
        self.centralLayout.setRowStretch(2, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "INPUT INFO"))
        self.weightLabel.setText(_translate("Form", "Weight"))
        self.descLabel.setText(_translate("Form", "Description"))
        self.submitBtn.setText(_translate("Form", "SUBMIT"))
