import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "INSERT INTO login(username, password) VALUES('Darshil','123456')"
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount,"Rows Inserted")
else:
    print("Error")
