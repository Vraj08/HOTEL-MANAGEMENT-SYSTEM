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
class WelcomeScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(WelcomeScreen, self).__init__()
        loadUi("LoginOptionMenu.ui", self)
        qpixmap = QPixmap("htl.png")
        qpixmap2 = QPixmap("htl2.png")
        qpixmap3 = QPixmap("Royal_Classic_Hotel_Logo11.png")
        self.imglbl.setPixmap(qpixmap)
        self.logo.setPixmap(qpixmap3)
        self.imglbl2.setPixmap(qpixmap2)
        self.loginbtn.clicked.connect(self.GotoLogin)
        self.signupbtn.clicked.connect(self.GotoCreateAcc)
    def GotoCreateAcc(self):
        login=CreateAccScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def GotoLogin(self):
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
class LoginScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(LoginScreen, self).__init__()
        loadUi("Login.ui", self)
        qpixmap= QPixmap("login-icon-3060.png")
        qpixmap2 = QPixmap("output-onlinepngtools.png")
        self.imglbl.setPixmap(qpixmap)
        self.imglbltwo.setPixmap(qpixmap2)
        self.Passwordledit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rspass.clicked.connect(self.rstpass)
        self.loginbtn.clicked.connect(self.validations)
    def rstpass(self):
        otp = ResetPass()
        widget.addWidget(otp)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def validations(self):
        lgid=self.Usernameledit.text()
        password =self.Passwordledit.text()
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vraj',
            port='3306',
            database='sgp'
        )
        mycur = mydb.cursor()
        query = 'SELECT Email_ID FROM logindetails'
        mycur.execute(query)
        dd = mycur.fetchall()
        if len(lgid)==0 and len(password)==0:
            self.errorlineedt.setText("Please Input all fields")
        elif len(lgid)==0:
            self.errorlineedt.setText("Please Enter Email-ID !")
        elif len(password)==0:
            self.errorlineedt.setText("Please Enter Password !")
        elif not ((lgid,) in dd):
            self.errorlineedt.setText("Email id not in system enter correct id ! ")
        else:
            query='SELECT Password FROM logindetails WHERE Email_ID=\''+lgid+"\'"
            mycur.execute(query)
            orgps=mycur.fetchone()
            orgpass=orgps[0]
            if orgpass== password:
                self.errorlineedt.setText("Login Successful! ")
                query = 'SELECT substr(RoleID,1,2) FROM logindetails WHERE Email_ID=\'' + lgid + "\'"
                mycur.execute(query)
                ab = mycur.fetchall()
                if(('RC',) == ab[0]):
                    rsta = RestaScreen()
                    widget.addWidget(rsta)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                if (('CL',) == ab[0]):
                    cln = CleaningScreen()
                    widget.addWidget(cln)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                if (('LN',) == ab[0]):
                    lnd = LaundaryScreen()
                    widget.addWidget(lnd)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                if (('RT',) == ab[0]):
                    rav = RoomAvailability()
                    widget.addWidget(rav)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.errorlineedt.setText("Invalid Password!")
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
            body = "We see you requested to CREATE A ACCOUNT IN ROYAL GALAXY here's one time password : " + Otp
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
        loadUi("EmailOTp.ui", self)
        self.signuplbl.clicked.connect(self.otptxt)
    def otptxt(self):
        print(self.ppotpp.text())
        print(Otp)
        if(self.ppotpp.text()!=Otp):
            self.errorlineedt.setText("\t\tInvalid Otp!")
        else:
            self.errorlineedt.setText("\t\tSign up Successful!")
class ResetPass(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(ResetPass, self).__init__()
        loadUi("resetpass.ui", self)
        self.Passwordleditwo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.fgtpass.clicked.connect(self.validations)
    def validations(self):
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
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vraj',
            port='3306',
            database='sgp'
        )
        mycur = mydb.cursor()
        query = 'SELECT Email_ID FROM logindetails'
        mycur.execute(query)
        dd = mycur.fetchall()
        print((lgid,) in dd)
        if len(lgid)==0 and len(password)==0 and len(passwordtwo)==0:
            self.errorlineedt.setText("Please Input all fields")
        elif len(lgid)==0:
            self.errorlineedt.setText("Please Enter Email ID !")
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
        elif not ((lgid,) in dd):
            self.errorlineedt.setText("Email id not in system enter correct id ! ")
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
            otp=ResetOtpScreen()
            widget.addWidget(otp)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            a = lgid
            b = password
            q2 = "UPDATE logindetails SET`Password` = (%s) WHERE `Email_ID` = (%s)"
            val2 = (b, a)
            mycur.execute(q2, val2)
            mydb.commit()
class ResetOtpScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(ResetOtpScreen, self).__init__()
        loadUi("OTP2.ui", self)
        self.signuplbl.clicked.connect(self.otptxt)
    def otptxt(self):
        print(self.ppotpp.text())
        print(Otp)
        if (self.ppotpp.text() != Otp):
            self.errorlineedt.setText("\t\tInvalid Otp!")
        else:
            self.errorlineedt.setText("\tPassword Changed Successfully!")


class RestaScreen(QDialog):  # it wiquantity inherit QDialog
    def __init__(self):  # Constructor
        super(RestaScreen, self).__init__()
        loadUi("Resta.ui", self)
        self.btn.clicked.connect(self.validations)

    def validations(self):
        quantity = []
        itemno = []
        d = 0
        # BEVERAGERS
        if (self.bv1.isChecked()):
            a = self.bv11.text()
            itemno.append('BV001')
            if a == '':
                self.error.setText("Please Enter Quantity in  MILKSHAKE")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MILKSHAKE (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv11.text())

        if (self.bv2.isChecked()):
            a = self.bv22.text()
            itemno.append('BV002')
            if a == '':
                self.error.setText("Please Enter Quantity in  COLD COFFEE WITH ICECREAM")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText(
                    "Please Enter Correct Quantity in  COLD COFFEE WITH ICECREAM (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv22.text())

        if (self.bv3.isChecked()):
            a = self.bv33.text()
            itemno.append('BV003')
            if a == '':
                self.error.setText("Please Enter Quantity in  COLD COFFEE")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  COLD COFFEE (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv33.text())

        if (self.bv4.isChecked()):
            a = self.bv44.text()
            itemno.append('BV004')
            if a == '':
                self.error.setText("Please Enter Quantity in  LASSI")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  LASSI (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv44.text())

        if (self.bv5.isChecked()):
            a = self.bv55.text()
            itemno.append('BV005')
            if a == '':
                self.error.setText("Please Enter Quantity in  BUTTER MILK")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BUTTER MILK (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv55.text())

        if (self.bv6.isChecked()):
            a = self.bv66.text()
            itemno.append('BV006')
            if a == '':
                self.error.setText("Please Enter Quantity in  AERATED WATER")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  AERATED WATER (Only Numbers Allowed !)")
            else:
                quantity.append(self.bv66.text())

        # SOUP
        if (self.so1.isChecked()):
            a = self.so11.text()
            itemno.append('SP001')
            if a == '':
                self.error.setText("Please Enter Quantity in  CHOICE OF SOUP")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  CHOICE OF SOUP (Only Numbers Allowed !)")
            else:
                quantity.append(self.so11.text())

        if (self.so2.isChecked()):
            a = self.so22.text()
            itemno.append('SP002')
            if a == '':
                self.error.setText("Please Enter Quantity in  ORIENTAL HOT ‘N’ SOUR")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  ORIENTAL HOT ‘N’ SOUR (Only Numbers Allowed !)")
            else:
                quantity.append(self.so22.text())

        if (self.so3.isChecked()):
            a = self.so33.text()
            itemno.append('SP003')
            if a == '':
                self.error.setText("Please Enter Quantity in  CHINESE MANCHOW ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  CHINESE MANCHOW (Only Numbers Allowed !)")
            else:
                quantity.append(self.so33.text())

        # BAKED DISH
        if (self.bd1.isChecked()):
            a = self.bd11.text()
            itemno.append('BD001')
            if a == '':
                self.error.setText("Please Enter Quantity in  BAKED MACARONI PINEAPPLE")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText(
                    "Please Enter Correct Quantity in  BAKED MACARONI PINEAPPLE (Only Numbers Allowed !)")
            else:
                quantity.append(self.bd11.text())

        if (self.bd2.isChecked()):
            a = self.bd22.text()
            itemno.append('BD002')
            if a == '':
                self.error.setText("Please Enter Quantity in  BAKED LASAGNA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BAKED LASAGNA (Only Numbers Allowed !)")
            else:
                quantity.append(self.bd22.text())

        # SALAD
        if (self.sa1.isChecked()):
            a = self.sa11.text()
            itemno.append('SD001')
            if a == '':
                self.error.setText("Please Enter Quantity in  GREEN SALAD")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  GREEN SALAD (Only Numbers Allowed !)")
            else:
                quantity.append(self.sa11.text())

        if (self.sa2.isChecked()):
            a = self.sa22.text()
            itemno.append('SD002')
            if a == '':
                self.error.setText("Please Enter Quantity in  NORMANDY CRUNCH")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  NORMANDY CRUNCH (Only Numbers Allowed !)")
            else:
                quantity.append(self.sa22.text())

        if (self.sa3.isChecked()):
            a = self.sa33.text()
            itemno.append('SD003')
            if a == '':
                self.error.setText("Please Enter Quantity in  GREEK SALAD")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  GREEK SALAD (Only Numbers Allowed !)")
            else:
                quantity.append(self.sa33.text())

        # Papad
        if (self.pa1.isChecked()):
            a = self.pa11.text()
            itemno.append('PD001')
            if a == '':
                self.error.setText("Please Enter Quantity in  ROASTED (PAPAD) ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  ROASTED (PAPAD)  (Only Numbers Allowed !)")
            else:
                quantity.append(self.pa11.text())

        if (self.pa2.isChecked()):
            a = self.pa22.text()
            itemno.append('PD002')
            if a == '':
                self.error.setText("Please Enter Quantity in  FRIED (PAPAD)")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  FRIED (PAPAD) (Only Numbers Allowed !)")
            else:
                quantity.append(self.pa22.text())

        if (self.pa3.isChecked()):
            a = self.pa33.text()
            itemno.append('PD003')
            if a == '':
                self.error.setText("Please Enter Quantity in  GREEK PALAD")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MASALA (PAPAD) (Only Numbers Allowed !)")
            else:
                quantity.append(self.pa33.text())

        # Curd
        if (self.cu1.isChecked()):
            a = self.cu11.text()
            itemno.append('CD001')
            if a == '':
                self.error.setText("Please Enter Quantity in  PLAIN CURD")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  PLAIN CURD  (Only Numbers Allowed !)")
            else:
                quantity.append(self.cu11.text())

        if (self.cu2.isChecked()):
            a = self.cu22.text()
            itemno.append('CD002')
            if a == '':
                self.error.setText("Please Enter Quantity in  VEG. RAITA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  VEG. RAITA (Only Numbers Allowed !)")
            else:
                quantity.append(self.cu22.text())

        if (self.cu3.isChecked()):
            a = self.cu33.text()
            itemno.append('CD003')
            if a == '':
                self.error.setText("Please Enter Quantity in  PUDINA RAITA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  PUDINA RAITA (Only Numbers Allowed !)")
            else:
                quantity.append(self.cu33.text())

        # kebab and starters
        if (self.ks1.isChecked()):
            a = self.ks11.text()
            itemno.append('KS001')
            if a == '':
                self.error.setText("Please Enter Quantity in  HARA BHARA KEBAB ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  HARA BHARA KEBAB  (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks11.text())

        if (self.ks2.isChecked()):
            a = self.ks22.text()
            itemno.append('KS002')
            if a == '':
                self.error.setText("Please Enter Quantity in  MAKHMALI PANEER TIKKA ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MAKHMALI PANEER TIKKA (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks22.text())

        if (self.ks3.isChecked()):
            a = self.ks33.text()
            itemno.append('KS003')
            if a == '':
                self.error.setText("Please Enter Quantity in  ACHARI BROCOLLI ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  ACHARI BROCOLLI (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks33.text())

        if (self.ks4.isChecked()):
            a = self.ks44.text()
            itemno.append('KS004')
            if a == '':
                self.error.setText("Please Enter Quantity in  LITCHI BHARWAN KEBAB ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  LITCHI BHARWAN KEBAB (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks44.text())

        if (self.ks5.isChecked()):
            a = self.ks55.text()
            itemno.append('KS005')
            if a == '':
                self.error.setText("Please Enter Quantity in  MULTANI PANEER TIKKA ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MULTANI PANEER TIKKA (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks55.text())

        if (self.ks6.isChecked()):
            a = self.ks66.text()
            itemno.append('KS006')
            if a == '':
                self.error.setText("Please Enter Quantity in  BUKHARA PUDINA ALOO ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BUKHARA PUDINA ALOO (Only Numbers Allowed !)")
            else:
                quantity.append(self.ks66.text())

        # tandoor
        if (self.tn1.isChecked()):
            a = self.tn11.text()
            itemno.append('TD001')
            if a == '':
                self.error.setText("Please Enter Quantity in  ROTI")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  ROTI (Only Numbers Allowed !)")
            else:
                quantity.append(self.tn11.text())

        if (self.tn2.isChecked()):
            a = self.tn22.text()
            itemno.append('TD002')
            if a == '':
                self.error.setText("Please Enter Quantity in  NAAN ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  NAAN (Only Numbers Allowed !)")
            else:
                quantity.append(self.tn22.text())

        if (self.tn3.isChecked()):
            a = self.tn33.text()
            itemno.append('TD003')
            if a == '':
                self.error.setText("Please Enter Quantity in  NAAN ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  NAAN (Only Numbers Allowed !)")
            else:
                quantity.append(self.tn33.text())

        # oriential main course
        if (self.om1.isChecked()):
            a = self.om11.text()
            itemno.append('OC001')
            if a == '':
                self.error.setText("Please Enter Quantity in  VEGETABLE EXOTICA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  VEGETABLE EXOTICA (Only Numbers Allowed !)")
            else:
                quantity.append(self.om11.text())

        if (self.om2.isChecked()):
            a = self.om22.text()
            itemno.append('OC002')
            if a == '':
                self.error.setText("Please Enter Quantity in  SCHEZWAN PANEER")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  SCHEZWAN PANEER (Only Numbers Allowed !)")
            else:
                quantity.append(self.om22.text())

        if (self.om3.isChecked()):
            a = self.om33.text()
            itemno.append('OC003')
            if a == '':
                self.error.setText("Please Enter Quantity in  CHINESE HOT POT")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  CHINESE HOT POT (Only Numbers Allowed !)")
            else:
                quantity.append(self.om33.text())

        # Indian Main Course
        if (self.im1.isChecked()):
            a = self.im11.text()
            itemno.append('IC001')
            if a == '':
                self.error.setText("Please Enter Quantity in  MANPASAND PANEER")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MANPASAND PANEER (Only Numbers Allowed !)")
            else:
                quantity.append(self.im11.text())

        if (self.im2.isChecked()):
            a = self.im22.text()
            itemno.append('IC002')
            if a == '':
                self.error.setText("Please Enter Quantity in  CHEESE CHILLY MASALA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  CHEESE CHILLY MASALA (Only Numbers Allowed !)")
            else:
                quantity.append(self.im22.text())

        if (self.im3.isChecked()):
            a = self.im33.text()
            itemno.append('IC003')
            if a == '':
                self.error.setText("Please Enter Quantity in  KARACHI KOFTA")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  KARACHI KOFTA (Only Numbers Allowed !)")
            else:
                quantity.append(self.im33.text())

        # DAL
        if (self.da1.isChecked()):
            a = self.da11.text()
            itemno.append('DL001')
            if a == '':
                self.error.setText("Please Enter Quantity in  MANPASAND TUVER DAL ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  MANPASAND TUVER DAL (Only Numbers Allowed !)")
            else:
                quantity.append(self.da11.text())

        if (self.da2.isChecked()):
            a = self.da22.text()
            itemno.append('DL002')
            if a == '':
                self.error.setText("Please Enter Quantity in  DAL MAKHANI ")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  DAL MAKHANI (Only Numbers Allowed !)")
            else:
                quantity.append(self.da22.text())

        # RICE
        if (self.rc1.isChecked()):
            a = self.rc11.text()
            itemno.append('RC001')
            if a == '':
                self.error.setText("Please Enter Quantity in  PULAO")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  PULAO (Only Numbers Allowed !)")
            else:
                quantity.append(self.rc11.text())

        if (self.rc2.isChecked()):
            a = self.rc22.text()
            itemno.append('RC002')
            if a == '':
                self.error.setText("Please Enter Quantity in  BASMATI RICE")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BASMATI RICE (Only Numbers Allowed !)")
            else:
                quantity.append(self.rc22.text())

        if (self.rc3.isChecked()):
            a = self.rc33.text()
            itemno.append('RC003')
            if a == '':
                self.error.setText("Please Enter Quantity in  DUM BIRYANI")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  DUM BIRYANI (Only Numbers Allowed !)")
            else:
                quantity.append(self.rc33.text())

        # DESSERT
        if (self.ds1.isChecked()):
            a = self.ds11.text()
            itemno.append('DS001')
            if a == '':
                self.error.setText("Please Enter Quantity in  ICE-CREAM")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  ICE-CREAM (Only Numbers Allowed !)")
            else:
                quantity.append(self.ds11.text())

        if (self.ds2.isChecked()):
            a = self.ds22.text()
            itemno.append('DS002')
            if a == '':
                self.error.setText("Please Enter Quantity in  BLACK FOREST BLAST")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BLACK FOREST BLAST (Only Numbers Allowed !)")
            else:
                quantity.append(self.ds22.text())

        if (self.ds3.isChecked()):
            a = self.ds33.text()
            itemno.append('DS003')
            if a == '':
                self.error.setText("Please Enter Quantity in  BROWNIE")
            if (not (a.isnumeric())) and (not (a == '')):
                self.error.setText("Please Enter Correct Quantity in  BROWNIE (Only Numbers Allowed !)")
            else:
                quantity.append(self.ds33.text())
        else:
            print('pt1:', itemno, quantity)
        # RoomNO
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
        rn = self.rn.text()
        if rn == '':
            self.rnerror.setText("Please Enter Room No.")

        elif not ((rn,) in rda) and (not (rn == '')):
            self.rnerror.setText("Please Enter Correct Room No.")
        else:
            self.rnerror.setText("")
            try:
                cnt = 0
                for i in range(len(itemno)):
                    if (quantity[i].isnumeric()):
                        cnt += 1
                query = 'SELECT Room_NO,Item_no,Quantity FROM foodorders'
                mycur.execute(query)
                alrd = mycur.fetchall()
                if (cnt == len(quantity)):
                    for i in range(len(itemno)):
                        query = 'SELECT Price FROM foodpricelist WHERE Item_No=\'' + itemno[i] + "\'"
                        mycur.execute(query)
                        ttl = int(mycur.fetchone()[0]) * int(quantity[i])
                        if ((rn, itemno[i], int(quantity[i]),) in alrd):
                            self.error.setText("Order Already Placed!")
                        else:
                            sql = "INSERT INTO foodorders (`Room_No`,`Item_no`,`Quantity`,`Total`) VALUES (%s, %s, %s, %s)"
                            val = (rn, itemno[i], int(quantity[i]), ttl)
                            mycur.execute(sql, val)
                            mydb.commit()
                            self.error.setText("Order Placed Successfully!")

            except:
                pass
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
class CleaningScreen(QDialog):  # it will inherit QDialog
    def __init__(self):  # Constructor
        super(CleaningScreen, self).__init__()
        loadUi("Cleaning.ui", self)
        self.tbl.setColumnWidth(0,150)
        self.tbl.setColumnWidth(1,410)
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
        query = 'SELECT * FROM cleaningdetails'
        mycur.execute(query)
        dd = mycur.fetchall()
        row=0
        self.tbl.setRowCount(len(dd))
        for ro in dd:
            self.tbl.setItem(row,0,QtWidgets.QTableWidgetItem(ro[0]))
            self.tbl.setItem(row,1, QtWidgets.QTableWidgetItem(ro[1]))
            row+=1

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
wlcmscrn = WelcomeScreen()  # Object of the class
widget = QStackedWidget()  # For Stacking multiple screens
widget.addWidget(wlcmscrn)
widget.setFixedHeight(1040)
widget.setFixedWidth(1920)
widget.show()
try:
    sys.exit(app.exec())
except:
  print("Exiting ... ")
