import smtplib
import random
gmail_user = 'royalgalaxy848@gmail.com'
gmail_password = 'Royal@Galaxy@88'
sent_from = gmail_user
#to = ['vrajpatel342008@gmail.com', '20ce102@charusat.edu.in', '20ce106@charusat.edu.in',  '20ce109@charusat.edu.in', '20ce110@charusat.edu.in', '20ce111@charusat.edu.in']
to='20ce110@charusat.edu.in'
subject = 'Password Reset Otp '
Otp=str(random.randint(10000,99999))
body = "We see you requested to change your password here's one time password : "+ Otp
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
    print ("Email sent successfully!")
except Exception as ex:
    print ("Otp not sent check email id or your internet connectivity… .",ex)