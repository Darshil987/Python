import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "DROP TABLE login"
    cursor.execute(sql)

else:
    print("ERROR")
