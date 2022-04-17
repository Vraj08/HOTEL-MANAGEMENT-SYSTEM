import mysql.connector
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
a='kaiparker666@gmail.com'
b='Vraj@1234'
q2="UPDATE logindetails SET`Password` = (%s) WHERE `Email_ID` = (%s)"
val2=(b,a)
mycur.execute(q2, val2)
mydb.commit()
'''fnrm = dd[len(dd) - 1][0][0:4] + str(int(dd[len(dd) - 1][0][4]) + 1)
print(fnrm)
sql = "INSERT INTO logindetails (`Email_ID`,`Password`,`RoleID`) VALUES (%s, %s, %s)"
sql2 = "INSERT INTO roles (`RoleID`,`RoleName`,`AssignedTo`) VALUES (%s, %s, %s);"
val = (lgid, password, fnrm)
val2 = (fnrm, rlnm, name)
print(val, val2)
mycur.execute(sql2, val2)
mycur.execute(sql, val)
mydb.commit()'''