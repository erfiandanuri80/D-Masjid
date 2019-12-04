from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
from PyQt5.QtSql import QSqlTableModel
import sqlite3
import code

class UiTakmir(QtWidgets.QDialog):
    def __init__(self):
        super(UiTakmir, self).__init__()
        uic.loadUi("infodialog.ui",self)
        self.pushButton_2.clicked.connect(self.backtomenu)
        self.setWindowModality(Qt.ApplicationModal)
        conn=sqlite3.connect('pemasukan_kas.db')
        c=conn.cursor()

        ketua=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Ketua Umum'")
        for x in ketua:
            hasil1=x[0]
        self.lineEdit.setText(str(hasil1))
        
        wkketua=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Wakil Ketua'")
        for x in wkketua:
            hasil2=x[0]
        self.lineEdit_7.setText(str(hasil2))
        
        dewan=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Dewan penasihat'")
        for x in dewan:
            hasil3=x[0]
        self.lineEdit_4.setText(str(hasil3))
        
        sekretaris=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Sekretaris'")
        for x in sekretaris:
            hasil4=x[0]
        self.lineEdit_2.setText(str(hasil4))

        wksekretaris=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Wakil Sekretaris'")
        for x in wksekretaris:
            hasil5=x[0]
        self.lineEdit_3.setText(str(hasil5))

        bendahara=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Bendahara'")
        for x in bendahara:
            hasil6=x[0]
        self.lineEdit_5.setText(str(hasil6))

        wkbendahara=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Wakil bendahara'")
        for x in wkbendahara:
            hasil7=x[0]
        self.lineEdit_6.setText(str(hasil7))

        bpendidikan=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Bidang Pendidikan'")
        for x in bpendidikan:
            hasil8=x[0]
        self.lineEdit_8.setText(str(hasil8))

        bpembangunan=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Bidang Pembangunan'")
        for x in bpembangunan:
            hasil9=x[0]
        self.lineEdit_9.setText(str(hasil9))

        bsosial=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Bidang Sosial'")
        for x in bsosial:
            hasil10=x[0]
        self.lineEdit_10.setText(str(hasil10))

        bperibadatan=c.execute("SELECT Nama FROM pengurus WHERE Jabatan='Bidang Peribadatan'")
        for x in bperibadatan:
            hasil11=x[0]
        self.lineEdit_11.setText(str(hasil11))

    def backtomenu(self):
        self.menu=code.Ui()
        self.menu.show()
        self.close()