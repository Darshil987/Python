import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="")
print(conn)
