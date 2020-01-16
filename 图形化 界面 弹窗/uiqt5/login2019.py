# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2019.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(login)
        self.textEdit.setGeometry(QtCore.QRect(140, 70, 131, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(login)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 130, 131, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 54, 12))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.pushButton.setText(_translate("login", "登录"))
        self.label.setText(_translate("login", "用户名"))
        self.label_2.setText(_translate("login", "密码"))
