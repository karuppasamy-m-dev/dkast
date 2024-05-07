#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = ("""create table emp_salary_details(id int NOT NULL AUTO_INCREMENT, empid varchar(20), year varchar(5), month varchar(15), salary int(10), workingdays int(10), presentdays int(10), leavedays int(10), gross_salary int(10), calcdate date, PRIMARY KEY (id))""")
cur.execute(query)
print("""
<script>
    alert("table created");
    location.href="./../index.py";
</script>
""")
dbconn.commit()
dbconn.close()
