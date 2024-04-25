#!C:/Users/karup/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconnect = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
conn = dbconnect.cursor()

tablecreate = ("""create table Emp_Details( id int NOT NULL AUTO_INCREMENT, EmpId varchar(100), EmpName varchar(100),EmpMailId varchar(100), EmpNumber int(10), Empdob date, EmpGender varchar(10), EmpAddress LONGTEXT, EmpPwd varchar(30), EmpDepart varchar(100), EmpSalary int(10), EmpImage varchar(600), PRIMARY KEY (id))""")
conn.execute(tablecreate)

print("""
<script>
    alert("Table Created");
</script>
""")


dbconnect.commit()
dbconnect.close()
