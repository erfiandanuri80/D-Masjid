from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
from PyQt5.QtSql import QSqlTableModel
import sqlite3
import adminpemasukan
from datetime import datetime

class Uiadding(QtWidgets.QDialog):
    def __init__(self):
        super(Uiadding, self).__init__()
        uic.loadUi('dialogadd.ui', self)
        hari= datetime.now().day
        bulan=datetime.now().month
        tahun=datetime.now().year
        self.setWindowTitle("add")
        self.pushButton.clicked.connect(self.add_data)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(tahun, bulan, hari+1), QtCore.QTime(0, 0, 0)))
        self.setWindowModality(Qt.ApplicationModal)        

    def add_data(self):
        ket=self.lineEdit.text()
        jenis=self.comboBox.currentText()
        tanggal=self.dateEdit.text()
        jumlah=self.lineEdit_2.text()
        query = QtSql.QSqlQuery()
        query.exec_("INSERT INTO catatan_kas (keterangan,tipe,tanggal,jumlah) values ('%s','%s','%s','%s')" %(ket,jenis,tanggal,jumlah))
        self.close()

class Uiaddingsub(QtWidgets.QDialog):
    def __init__(self):
        super(Uiaddingsub, self).__init__()
        uic.loadUi('dialogsub.ui', self)
        hari= datetime.now().day
        bulan=datetime.now().month
        tahun=datetime.now().year
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(tahun, bulan, hari+1), QtCore.QTime(0, 0, 0)))
        self.setWindowTitle("add")
        self.pushButton.clicked.connect(self.add_data)
        self.setWindowModality(Qt.ApplicationModal)        

    def add_data(self):
        ket=self.lineEdit.text()
        jenis=self.comboBox.currentText()
        tanggal=self.dateEdit.text()
        jumlah=self.lineEdit_2.text()
        query = QtSql.QSqlQuery()
        query.exec_("INSERT INTO catatan_kaskeluar (keterangan,tipe,tanggal,jumlah) values ('%s','%s','%s','%s')" %(ket,jenis,tanggal,jumlah))
        self.close()

class Uiaddingzakat(QtWidgets.QDialog):
    def __init__(self):
        super(Uiaddingzakat, self).__init__()
        uic.loadUi('dialogaddzakat.ui', self)
        hari= datetime.now().day
        bulan=datetime.now().month
        tahun=datetime.now().year
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(tahun, bulan, hari+1), QtCore.QTime(0, 0, 0)))
        self.setWindowTitle("zakat")
        self.pushButton.clicked.connect(self.add_data)
        self.setWindowModality(Qt.ApplicationModal)

    def add_data(self):
        ket=self.lineEdit.text()
        jenis=self.comboBox.currentText()
        tanggal=self.dateEdit.text()
        jumlah=self.lineEdit_2.text()
        query = QtSql.QSqlQuery()
        query.exec_("INSERT INTO catatan_zakat (muzakki,tipe,tanggal,jumlah) values ('%s','%s','%s','%s')" %(ket,jenis,tanggal,jumlah))
        self.close()
        