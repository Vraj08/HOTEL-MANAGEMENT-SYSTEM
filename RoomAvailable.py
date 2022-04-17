import sys
import re
from PyQt5.uic import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector
class RoomAvailability(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(RoomAvailability, self).__init__()
        loadUi("RoomBookings.ui", self)
        self.tbl.setColumnWidth(0,150)
        self.tbl.setColumnWidth(1,200)
        self.tbl.setColumnWidth(2, 210)
        self.loaddata()
    def loaddata(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vraj',
            port='3306',
            database='sgp'
        )
        mycur = mydb.cursor()
        query = "SELECT * FROM roombookings"
        mycur.execute(query)
        dd = mycur.fetchall()
        row=0
        self.tbl.setRowCount(len(dd))
        for ro in dd:
            self.tbl.setItem(row,0,QtWidgets.QTableWidgetItem(ro[0]))
            self.tbl.setItem(row,2, QtWidgets.QTableWidgetItem(ro[1]))
            self.tbl.setItem(row, 1, QtWidgets.QTableWidgetItem(ro[2]))
            row+=1
# main
app = QApplication(sys.argv)  # for Launching the app pass sys.argv i.e commandline argument
wlcmscrn = RoomAvailability()  # Object of the class
widget = QStackedWidget()  # For Stacking multiple screens
widget.addWidget(wlcmscrn)
widget.setFixedHeight(1040)
widget.setFixedWidth(1920)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting ... ")
