import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "SELECT\
           login.username as user,\
           cart.product as product\
           FROM login\
           INNER JOIN cart ON login.username=cart.username"
    cursor.execute(sql)
    x = cursor.fetchall()
    for i in x:
        print(i)
else:
    print("Error")
