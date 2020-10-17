import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "SELECT * FROM login ORDER BY password"
    cursor.execute(sql)
    x = cursor.fetchall()
    for i in x:
        print(i)
else:
    print("Error")
