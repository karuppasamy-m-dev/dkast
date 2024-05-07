#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = ("""CREATE TABLE emp_leave_detailes(id INT NOT NULL AUTO_INCREMENT, empid VARCHAR(30), empname VARCHAR(50), reasontype VARCHAR(3), reason VARCHAR(200), fromleave DATE, toleave DATE, dayscount INT(10), avilcount INT(10), status varchar(50), paidornot varchar(5), PRIMARY KEY(id))""")
cur.execute(query)
print("""
<script>
    alert("table created");
    location.href="./../index.py";
</script>
""")
dbconn.commit()
dbconn.close()
