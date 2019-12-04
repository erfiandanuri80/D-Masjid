from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
from PyQt5.QtSql import QSqlTableModel
import sqlite3
import code, adminpengeluaran,adminzakat,adding

conn=sqlite3.connect('pemasukan_kas.db')
c=conn.cursor()

class UiAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiAdmin, self).__init__()
        uic.loadUi('dasaradmin.ui', self)
        self.model = QtSql.QSqlTableModel()
        self.pushButton.clicked.connect(self.showkeluar)
        self.Zakat3_2.clicked.connect(self.showzakat)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.remove)
        self.pushButton_5.clicked.connect(self.backtomenu)
        self.displaytable()
    

        datamasuk=c.execute("SELECT SUM(jumlah) FROM catatan_kas  ")
        for x in datamasuk:
            hasil1=x[0]
        self.lineEdit_2.setText(str(hasil1))

        datakeluar=c.execute("SELECT SUM(jumlah) FROM catatan_kaskeluar ")
        for y in datakeluar:
            hasil2=y[0]
        self.lineEdit_3.setText(str(hasil2))
        
        if hasil2 == None :
            self.lineEdit_4.setText(str(hasil2))
        if hasil1== None :
            self.lineEdit_4.setText("-"+str(hasil2))
        else:
            hasil3=hasil1-hasil2
            self.lineEdit_4.setText(str(hasil3))

        datazakat=c.execute("SELECT SUM(jumlah) FROM catatan_zakat ")
        for a in datazakat:
            hasil4=a[0]
        self.Zakat2_2.setText(str(hasil4))

    def add(self):
        self.addrow=adding.Uiadding()
        self.addrow.show()
        self.displaytable()

    def showzakat(self):
        self.zakatwindow=adminzakat.UiAdminZakat()
        self.close()
        self.zakatwindow.show()
    
    def showkeluar(self):
        self.pengeluaranwindow=adminpengeluaran.UiAdminPengeluaran()
        self.close()
        self.pengeluaranwindow.show()
   
    def displaytable(self):
        self.model.setTable('catatan_kas')
        self.model.select()
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

        datamasuk=c.execute("SELECT SUM(jumlah) FROM catatan_kas  ")
        for x in datamasuk:
            hasil1=x[0]
        self.lineEdit_2.setText(str(hasil1))

        datakeluar=c.execute("SELECT SUM(jumlah) FROM catatan_kaskeluar ")
        for y in datakeluar:
            hasil2=y[0]
        self.lineEdit_3.setText(str(hasil2))
        
        if hasil2 == None :
            self.lineEdit_4.setText(str(hasil2))
        if hasil1== None :
            self.lineEdit_4.setText("-"+str(hasil2))
        else:
            hasil3=hasil1-hasil2
            self.lineEdit_4.setText(str(hasil3))

    def remove(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.displaytable()
    
    def backtomenu(self):
        self.dasar=code.Ui()
        self.dasar.show()
        self.close()
