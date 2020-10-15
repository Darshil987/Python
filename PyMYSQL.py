import mysql.connector as mcom

conn = mcom.connect(host="localhost", user="root", password="", database="abc")
if conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE login(srno INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(8), password VARCHAR(20))")
else:
    print("Error")
