import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "SELECT * FROM login WHERE username=%s"
    val = 'Darshil',
    cursor.execute(sql, val)
    x = cursor.fetchall()
    for i in x:
        print(i)
else:
    print("Error")
