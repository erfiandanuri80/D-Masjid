from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import sys
from PyQt5.QtSql import QSqlTableModel
import sqlite3
import adminpengeluaran, adminpemasukan, adminzakat, adding, login, takmir, calczakatmal

## MAIN WINDOW ##
        
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.model = QSqlTableModel()
        uic.loadUi('dasar.ui', self)
        self.show()
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.Login.clicked.connect(self.login)
        self.Takmir.clicked.connect(self.showTakmir)
        self.pushButton.clicked.connect(self.infokas)
        self.pushButton_2.clicked.connect(self.infokaskeluar)
        self.Zakat3_2.clicked.connect(self.infozakat)
        self.hitung.clicked.connect(self.calc)
        self.displaytable()
        conn=sqlite3.connect('pemasukan_kas.db')
        c=conn.cursor()

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
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('pemasukan_kas.db')
        if not db.open():
            self.statusBar().showMessage('connection database error')
            #self.label.setText("connection database error")
            return False
        else:
            self.statusBar().showMessage('connection database ready')
            #self.label.setText("connection database ready")
            return True
    def displaytable(self):
        self.model.setTable('catatan_kas')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
    def infokas(self):
        query = QtSql.QSqlQuery("SELECT * FROM catatan_kas ")
        self.model.setQuery(query)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
    def infokaskeluar(self):
        query = QtSql.QSqlQuery("SELECT * FROM catatan_kaskeluar ")
        self.model.setQuery(query)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
    def infozakat(self):
        query = QtSql.QSqlQuery("SELECT * FROM catatan_zakat ")
        self.model.setQuery(query)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()     
    def showTakmir(self):
        self.info=takmir.UiTakmir()
        self.close()
        self.info.show()
    def login(self):
        self.log=login.UiLogin()
        self.close() 
        self.log.show()
    def calc(self):
        self.calcshow=calczakatmal.Uikalkulatorzakatmal()
        self.calcshow.show()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
