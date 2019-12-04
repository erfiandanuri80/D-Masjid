from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
from PyQt5.QtSql import QSqlTableModel
import sqlite3
import code

class Uikalkulatorzakatmal(QtWidgets.QDialog):
    def __init__(self):
        super(Uikalkulatorzakatmal, self).__init__()
        uic.loadUi('kalkulatorzakatmal.ui', self)
        self.setWindowTitle("Kalkulator Zakat Mal")
        self.pushButton.clicked.connect(self.hitung)
        self.pushButton_2.clicked.connect(self.zakatprofesi)
        self.setWindowModality(Qt.ApplicationModal)
        nsb= 85*660485
        self.lineEdit_7.setText(str(nsb))
    def zakatprofesi(self):
        self.showzakatprofesi=Uikalkulatorzakatprofesi()
        self.close()
        self.showzakatprofesi.show()
    def hitung(self):
        input1=self.lineEdit.text()
        input2=self.lineEdit_2.text()
        input3=self.lineEdit_3.text()
        input4=self.lineEdit_4.text()
        input5=self.lineEdit_5.text()
        nisab=self.lineEdit_7.text()
        print(input1,input2,input3,input4,input5)
        if input1 == "":
            input1 = 0
        if input2 == "":
            input2 = 0
        if input3 == "":
            input3 = 0
        if input4 == "":
            input4 = 0
        if input5 == "":
            input5 = 0
        output1=int(input1)+int(input2)+int(input3)+int(input4)-int(input5)
        self.lineEdit_6.setText(str(output1))
        if output1 > int(nisab):
            output2 = int(output1*0.025)
            self.lineEdit_8.setText(str(output2))
        else:
            self.lineEdit_8.setText("0")
    
        
        
class Uikalkulatorzakatprofesi(QtWidgets.QDialog):
    def __init__(self):
        super(Uikalkulatorzakatprofesi, self).__init__()
        uic.loadUi('kalkulatorzakatprofesi.ui', self)
        self.setWindowTitle("Kalkulator Zakat profesi")
        self.pushButton.clicked.connect(self.hitung)
        self.pushButton_2.clicked.connect(self.zakatmal)
        self.setWindowModality(Qt.ApplicationModal)
        nsb= int((85*660485)/12)
        self.lineEdit_7.setText(str(nsb))

    def zakatmal(self):
        self.showzakatmal=Uikalkulatorzakatmal()
        self.close()
        self.showzakatmal.show()
    def hitung(self):
        input1=self.lineEdit_2.text()
        input2=self.lineEdit_3.text()
        input3=self.lineEdit_4.text()
        nisab=self.lineEdit_7.text()
        print(input1,input2,input3)
        if input1 == "":
            input1 = 0
        if input2 == "":
            input2 = 0
        if input3 == "":
            input3 = 0
        nisab=int(nisab)
        output1=int(input1)+int(input2)-int(input3)
        self.lineEdit_6.setText(str(output1))
        if output1 > nisab:
            output2 = int(output1*0.025)
            self.lineEdit_8.setText(str(output2))
        else:
            self.lineEdit_8.setText("0")
