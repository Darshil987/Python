import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="")
cursor = conn.cursor()

cursor.execute("CREATE DATABASE abc")
