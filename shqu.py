import mysql.connector
mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='vraj',
                port='3306',
                database='sgp'
            )
mycur = mydb.cursor()
lgid="20ce111@charusat.edu.in"
query = 'SELECT substr(RoleID,1,2) FROM logindetails WHERE Email_ID=\'' + lgid + "\'"
mycur.execute(query)
ab =mycur.fetchall()
print(ab)
print(('RC',)==ab[0])
'''bb = 'MN001'
lgid='asdcjnswdv'
password='xuidcuidweco'
rlnm='Receptionist'
query='SELECT RoleID FROM roles WHERE RoleName=\''+rlnm+"\'"
mycur.execute(query)
dd=mycur.fetchall()
fnrm=dd[len(dd)-1][0][0:4]+str(int(dd[len(dd)-1][0][4])+1)
print(fnrm)
val=('vrajpatel22@gmail.com', 'Vraj@3321', 'RT004')
val2=('RT004', 'Receptionist', 'Vraj Patel')
sql = "INSERT INTO logindetails (`Email_ID`,`Password`,`RoleID`) VALUES (%s, %s, %s)"
sql2="INSERT INTO roles (`RoleID`,`RoleName`,`AssignedTo`) VALUES (%s, %s, %s);"
#val = (lgid, password, bb)
#val2=(bb,'Manager','Raghu')
print(val,val2)
#try:
mycur.execute(sql2, val2)
mycur.execute(sql, val)
mydb.commit()
self.errorlineedt.setText("Id Created Successfully ! ")
#except:
self.errorlineedt.setText("Id Already Exists ! ")
'''