import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "DELETE FROM login WHERE username='Darshil'"
    cursor.execute(sql)
    conn.commit()
else:
    print("Error")
