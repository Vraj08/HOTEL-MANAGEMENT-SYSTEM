import sys
import re
from PyQt5.uic import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import smtplib
import random
import mysql.connector
class WelcomeScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(WelcomeScreen, self).__init__()
        loadUi("CreateAccount.ui", self)
        qpixmap= QPixmap("Sign_up_today.png")
        qpixmap2 = QPixmap("jing.fm-psychologist-clip-art-3981675.png")
        self.imglbl.setPixmap(qpixmap)
        self.imglbltwo.setPixmap(qpixmap2)
        self.Passwordleditwo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signuplbl.clicked.connect(self.validations)
    def validations(self):
        Otp = str(random.randint(10000, 99999))
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
        def checkotp(lgid):
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
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            return 0
        lgid=self.Usernameledit.text()
        password =self.Passwordledit.text()
        passwordtwo=self.Passwordleditwo.text()
        if len(lgid)==0 and len(password)==0 and len(passwordtwo)==0:
            self.errorlineedt.setText("Please Input all fields")
        elif len(lgid)==0:
            self.errorlineedt.setText("Please Enter username !")
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
      #  elif checkotp(lgid):
      #      self.errorlineedt.setText("Otp not sent check email id or your internet connectivity… .")
        else:
           # role = self.fld.currentText()
            print(slef.otp.text(),Otp)
            if slef.otp.text() != Otp:
                self.errorlineedt.setText("Otp not matching… ")
            '''mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='vraj',
                port='3306',
                database='sgp'
            )
            mycur = mydb.cursor()
            bb='MN001'
            sql = "INSERT INTO logindetails (`Email_ID`,`Password`,`RoleID`) VALUES (%s,%s,%s)"
            val = (lgid, password,bb)
            print(val)'''
            #try:
            mycur.execute(sql, val)
            mydb.commit()
            self.errorlineedt.setText("Id Created Successfully ! ")
            #except:
            self.errorlineedt.setText("Id Already Exists ! ")
# main
app = QApplication(sys.argv)  # for Launching the app pass sys.argv i.e commandline argument
wlcmscrn = WelcomeScreen()  # Object of the class
widget = QStackedWidget()  # For Stacking multiple screens
widget.addWidget(wlcmscrn)
widget.setFixedHeight(1040)
widget.setFixedWidth(1920)
widget.show()
#try:
sys.exit(app.exec())
#except:
print("Exiting ... ")