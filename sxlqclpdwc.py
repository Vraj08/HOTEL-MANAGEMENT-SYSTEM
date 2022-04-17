import mysql.connector
mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='vraj',
                port='3306',
                database='sgp'
            )
mycur = mydb.cursor()
iteamno=['DL001','DL002']
Quantity=['1','2']
RoomNo='SD11'
query = 'SELECT Room_NO,Item_no,Quantity FROM foodorders'
mycur.execute(query)
rda=mycur.fetchall()
print(rda)
a='SD11'
b='DL002'
c=33
print((a,b,c,) in rda)
""""a='SS11'
print((a,) in rda)
for i in range(len(iteamno)):
    query='SELECT Price FROM foodpricelist WHERE Item_No=\''+iteamno[i]+"\'"
    mycur.execute(query)
    ttl=int(mycur.fetchone()[0])*int(Quantity[i])
    sql = "INSERT INTO foodorders (`Room_No`,`Item_no`,`Quantity`,`Total`) VALUES (%s, %s, %s, %s)"
    val = (RoomNo, iteamno[i], int(Quantity[i]), ttl)
    mycur.execute(sql, val)
    mydb.commit()
#try:
sql = "INSERT INTO foodorders (`Room_No`,`Item_no`,`Quantity`,`Total`) VALUES (%s, %s, %s, %s)"
print(sql)
for i in range(len(iteamno)):
    val = (RoomNo, iteamno[i], int(Quantity[i]), Total)
    mycur.execute(sql, val)
    mydb.commit()
#except:
print()
"""