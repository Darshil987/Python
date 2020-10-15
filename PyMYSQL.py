import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    sql = "INSERT INTO login(username, password) VALUES(%s,%s)"
    val =[
        ('Darshil1','132'),
        ('Darshil12','123'),
        ('Darshil13','312'),
    ]
    cursor.executemany(sql, val)
    conn.commit()
    print(cursor.rowcount,"Rows Inserted")
else:
    print("Error")
