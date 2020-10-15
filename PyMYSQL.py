import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="")
cursor =conn.cursor()

cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
