import sys
import re
from PyQt5.uic import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector
class LaundaryScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(LaundaryScreen, self).__init__()
        loadUi("Laundary.ui", self)
        self.loginbtn.clicked.connect(self.validations)
    def validations(self):
        qn = self.qnty.text()
        rn = self.rnno.text()
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vraj',
            port='3306',
            database='sgp'
        )
        mycur = mydb.cursor()
        query = 'SELECT Room_NO FROM customerdata'
        mycur.execute(query)
        rda = mycur.fetchall()
        if rn == '':
            self.errorlineedt.setText("Please Enter Room No.")
        elif qn=='':
            self.errorlineedt.setText("Please Enter Quantity")
        elif not ((rn,) in rda) and (not (rn == '')):
            self.errorlineedt.setText("Please Enter Correct Room No.")
        elif not (qn.isnumeric()):
            self.errorlineedt.setText("Please Enter Correct Quantity Only Numbers Allowed!!")
        else:
            self.errorlineedt.setText("")
            ttl=int(qn)*20
            '''query = 'SELECT * FROM laundrydetails WHERE Room_No=\'' + rn + "\'"
            mycur.execute(query)
            dd=mycur.fetchall()
            if ((rn, qn, ttl,) in dd):
                self.errorlineedt.setText("Already Submitted!")'''
            try:
                query = "INSERT INTO laundrydetails (`Room_No`,`Quantity`,`Total`) VALUES (%s, %s, %s)"
                val = (rn, qn, ttl)
                mycur.execute(query, val)
                mydb.commit()
                self.errorlineedt.setText("Submitted Successfully!")
            except:
                self.errorlineedt.setText("Already Submitted!")
app = QApplication(sys.argv)  # for Launching the app pass sys.argv i.e commandline argument
wlcmscrn = LaundaryScreen()  # Object of the class
widget = QStackedWidget()  # For Stacking multiple screens
widget.addWidget(wlcmscrn)
widget.setFixedHeight(1040)
widget.setFixedWidth(1920)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting ... ")