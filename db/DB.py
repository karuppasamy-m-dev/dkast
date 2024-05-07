#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb


cgitb.enable()
serverconnect = pymysql.connect(host="localhost", user="root", password="")
conn = serverconnect.cursor()

dbcreate = """create database dkast_py_site"""
conn.execute(dbcreate)
print("""
<script>
    alert("Database Created");
</script>
""")
serverconnect.commit()
serverconnect.close()