#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgitb

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

# dropqu = """drop table user_details"""
# cur.execute(dropqu)

createqu = """CREATE TABLE user_details(id INT NOT NULL AUTO_INCREMENT, userid varchar(50), username varchar(100), useremail varchar(100), userdob date, usernumber BIGINT(10), profession varchar(50), address varchar(200), pincode varchar(20), password varchar(50), PRIMARY KEY(id))"""
cur.execute(createqu)

if createqu:
    print("""
    <script>
        alert("user table created");
        window.location.href="./../index.py";
    </script>
    """)
else:
    print("""
        <script>
            alert("Error in user table created");
            window.location.href="./../index.py";
        </script>
        """)
