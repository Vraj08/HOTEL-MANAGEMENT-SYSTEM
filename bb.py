import sys
import re
import smtplib
import random
from PyQt5.uic import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector
Otp = str(random.randint(10000, 99999))
class CreateAccScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(CreateAccScreen, self).__init__()
        loadUi("CreateAccount.ui", self)
        qpixmap= QPixmap("Sign_up_today.png")
        qpixmap2 = QPixmap("jing.fm-psychologist-clip-art-3981675.png")
        self.imglbl.setPixmap(qpixmap)
        self.imglbltwo.setPixmap(qpixmap2)
        self.Passwordleditwo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signuplbl.clicked.connect(self.validations)
    def validations(self):
        def abcd():
            otp = OTPScreen()
            print(Otp)
            print('b')
        def check(passwd):
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            mat = re.search(pat,passwd)
            if mat:
                return 0
            else:
                return 1
        def checktwo(email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (re.fullmatch(regex, email)):
                return 0
            else:
                return 1
        lgid=self.Usernameledit.text()
        password =self.Passwordledit.text()
        passwordtwo=self.Passwordleditwo.text()
        name=self.name.text()
        fild=self.fld.currentText()
        if len(lgid)==0 and len(password)==0 and len(passwordtwo)==0 and len(name)==0:
            self.errorlineedt.setText("Please Input all fields")
        elif len(lgid)==0:
            self.errorlineedt.setText("Please Enter Email ID !")
        elif len(name) == 0:
            self.errorlineedt.setText("Please Enter Name !")
        elif len(password)==0:
            self.errorlineedt.setText("Please Enter Password !")
        elif len(passwordtwo) == 0:
            self.errorlineedt.setText("Please Enter Confirm Password !")
        elif checktwo(lgid):
            self.errorlineedt.setText("Please Enter Correct Email ID ! ")
        elif passwordtwo!=password:
            self.errorlineedt.setText("Passwords Don't Match ! ")
        elif check(password):
            self.errorlineedt.setText("Password Doesn't meet Required Conditions ! ")
        else:
            gmail_user = 'royalgalaxy848@gmail.com'
            gmail_password = 'Royal@Galaxy@88'
            sent_from = gmail_user
            to = lgid
            subject = 'Password Reset Otp '
            body = "We see you requested to change your password here's one time password : " + Otp
            email_text = """\
                        From: %s
                        To: %s
                        Subject: %s

                        %s
                        """ % (sent_from, ", ".join(to), subject, body)
            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                self.errorlineedt.setText("Email sent successfully!")
            except:
                self.errorlineedt.setText("Otp not sent check email id or your internet connectivity… .")
            otp=OTPScreen()
            widget.addWidget(otp)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='vraj',
                port='3306',
                database='sgp'
            )
            mycur = mydb.cursor()
            rlnm=fild[6:len(fild)-1]
            query = 'SELECT RoleID FROM roles WHERE RoleName=\'' + rlnm + "\'"
            mycur.execute(query)
            dd = mycur.fetchall()
            fnrm = dd[len(dd) - 1][0][0:4] + str(int(dd[len(dd) - 1][0][4]) + 1)
            print(fnrm)
            sql = "INSERT INTO logindetails (`Email_ID`,`Password`,`RoleID`) VALUES (%s, %s, %s)"
            sql2 = "INSERT INTO roles (`RoleID`,`RoleName`,`AssignedTo`) VALUES (%s, %s, %s);"
            val = (lgid, password, fnrm)
            val2 = (fnrm, rlnm, name)
            print(val, val2)
            mycur.execute(sql2, val2)
            mycur.execute(sql, val)
            mydb.commit()
class OTPScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(OTPScreen, self).__init__()
        loadUi("OTP2.ui", self)
        self.signuplbl.clicked.connect(self.otptxt)
    def otptxt(self):
        print(self.ppotpp.text())
        print(Otp)
        if (self.ppotpp.text() != Otp):
            self.errorlineedt.setText("\t\tInvalid Otp!")
        else:
            self.errorlineedt.setText("\tPassword Changed Successfully!")
# main
app = QApplication(sys.argv)  # for Launching the app pass sys.argv i.e commandline argument
wlcmscrn = CreateAccScreen()  # Object of the class
widget = QStackedWidget()  # For Stacking multiple screens
widget.addWidget(wlcmscrn)
widget.setFixedHeight(1040)
widget.setFixedWidth(1920)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting ... ")
