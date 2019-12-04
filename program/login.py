from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
import code, adminpemasukan

class UiLogin(QtWidgets.QDialog):
    def __init__(self):
        super(UiLogin, self).__init__()
        uic.loadUi('login.ui', self)
        self.setWindowTitle("Login")
        self.pushButton_2.clicked.connect(self.backtomenu)
        self.pushButton.clicked.connect(self.func)
        self.setWindowModality(Qt.ApplicationModal)
    def func(self):
        username="admin"
        password="123"
        inusername=self.lineEdit.text()
        inpassword=self.lineEdit_2.text()
        if ((inusername == "admin") and (inpassword =="123")):
            self.homeadmin=adminpemasukan.UiAdmin()
            self.homeadmin.show()
            self.close()
        else:
            self.label_4.setText("error")

    def backtomenu(self):
        self.dasar=code.Ui()
        self.dasar.show()
        self.close()        