<<<<<<< HEAD
#!C:/Users/karup/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = ("""create table Emp_Inventory(id int NOT NULL AUTO_INCREMENT, VidId varchar(100), VidName varchar(100), VidTitle varchar(100), VidChapter varchar(100), VidUpdate date, VidSrc varchar(100), VidDesc varchar(300), VidNotes varchar(500), VidTask varchar(400), VidStatus varchar(10), VidComments varchar(100), uploadBy varchar(20), PRIMARY KEY (id))""")
cur.execute(query)
print("""
<script>
    alert("table created");
    location.href="./../EmpInventoryAdd.py";
</script>
""")
dbconn.commit()
dbconn.close()
=======
#!C:/Users/karup/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = ("""create table Emp_Inventory(id int NOT NULL AUTO_INCREMENT, VidId varchar(100), VidName varchar(100), VidTitle varchar(100), VidChapter varchar(100), VidUpdate date, VidSrc varchar(100), VidDesc varchar(300), VidNotes varchar(500), VidTask varchar(400), VidStatus varchar(10), VidComments varchar(100), uploadBy varchar(20), PRIMARY KEY (id))""")
cur.execute(query)
print("""
<script>
    alert("table created");
    location.href="./../EmpInventoryAdd.py";
</script>
""")
dbconn.commit()
dbconn.close()
>>>>>>> f3269295653c72b5eea73b89f09119481450d980
