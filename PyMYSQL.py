import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "UPDATE login SET username='Darshil' WHERE username='Darshil1'"
    cursor.execute(sql)
    conn.commit()
else:
    print("Error")
