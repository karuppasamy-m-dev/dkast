#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
import cgi, cgitb, pymysql

print("content-type:text/html \r\n\r\n")

form = cgi.FieldStorage()
uid = form.getvalue('id')

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = """select userid from user_details where id = '%s' """ % uid
cur.execute(query)
getuid = cur.fetchone()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dkast</title>
    <link rel="stylesheet" href="./Resources/style.css">
    <link rel="shortcut icon" href="./Resources/images/logo.png" type="image/x-icon">
    <!-- boostrap css -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <!-- fontawsome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <div class="container-fluid">
        <div class="usparent d-flex">
            <div class="usnav py-4">
                <div class="w-100 h-100 d-grid align-items-betwwen justify-content-center">
                    <div class="logo">
                        <a href="./Index.py"><img src="./Resources/images/logo.png" alt="" width="60px"></a>
                    </div>
                    <div class="nav d-grid align-items-between justify-content-center">
                        <a href="./UserDashboard.py?id=%s"><i class="fa-solid fa-chalkboard-user"
                                style="color: #162133; font-size: 20px;"></i></a>
                        <a href="UserOnGoingCourse.py?id=%s"><i class="fa-solid fa-table-columns"
                                style="color: #162133; font-size: 20px;"></i></a>
                        <a href="UserCourseList.py?id=%s"><i class="fa-solid fa-chart-line" style="color: #162133; font-size: 20px;"></i></a>
                    </div>""" % (uid, uid, uid))
print("""                    
                    <div class="profile" id="profile-full">
                        <div class="profile-hid d-none" id="profile-hid">
                            <div class="profile-in" id="profile-in">
                                <a href="./UserProfileEdit.py"><i class="fa-solid fa-gear"
                                        style="color: #162133; font-size: 20px;"></i></a>
                                <a type="button" data-bs-target="#password_change_modal" data-bs-toggle="modal"><i
                                        class="fa-solid fa-key" style="color: #162133; font-size: 20px;"></i></a>
                                <a href="./Index.py"><i class="fa-solid fa-right-from-bracket"
                                        style="color: #162133; font-size: 20px;"></i></a>
                            </div>
                        </div>
                        <span class="profile-view d-flex justify-content-center pt-4" id="profile-view"><i
                                class="fa-regular fa-circle-user" style="color: #162133; font-size: 30px;"></i></span>
                    </div>
                </div>
            </div>
            <div class="uscontent">
                <div class="container py-5" id="courselisttable">
                    <table class="table table-hover">
                        <thead>
                            <tr class="text-center">
                                <th scope="col" class="py-3">Sno</th>
                                <th scope="col" class="py-3">Course Name</th>
                                <th scope="col" class="py-3">Start Date</th>
                                <th scope="col" class="py-3">End Date</th>
                                <th scope="col" class="py-3">Status</th>                            
                            </tr>
                        </thead>
                        <tbody>""")
query1 = """select * from course_enroll where empid = '%s'""" % getuid
cur.execute(query1)
data = cur.fetchall()
for i in data:
    print("""                        
                            <tr class="text-center">
                                <th scope="row" class="py-3">%s</th>
                                <td class="py-3">%s</td>
                                <td class="py-3">%s</td>
                                <td class="py-3">%s</td>
                                <td class="py-3">Click to Continue <a href="UserOnGoingCourse.py?id=%s&title=%s&status=%s" class="">%s</a></td>
                            </tr>""" % (i[0], i[1], i[2], i[3], uid, i[1], i[4], i[4]))
dbconn.commit()
dbconn.close()
print("""                                                
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" id="password_change_modal" aria-hidden="true" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-body p-5">
                    <form method="post" name="password_change" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="oldpass" class="form-label">Enter Your Old Password</label>
                            <input type="text" name="oldpass" id="oldpass" class="form-control">
                        </div>
                        <div class="mb-3">
                            <label for="newpass" class="form-label">Enter New Password</label>
                            <input type="password" name="newpass" id="newpass" class="form-control">
                        </div>
                        <div class="mb-2">
                            <label for="newconpass" class="form-label">Confirm your Password</label>
                            <input type="password" name="newconpass" id="newconpass" class="form-control">
                        </div>
                        <div class="d-flex mb-4">
                            <input type="checkbox" name="showpass" id="showpass" class="form-check-input me-2">
                            <label for="showpass" class="form-check-label">Show Password</label>
                        </div>
                        <div class="d-flex justify-content-center ">
                            <input type="submit" value="Submit" name="passchbtn" class="btn add-btn px-4">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <script>
        var showpasscheck = document.forms['password_change']['showpass'];
        var passcon = document.forms['password_change']['newconpass'];
        var newpass = document.forms['password_change']['newpass'];
        showpasscheck.onclick = function () {
            if (this.checked) {
                passcon.type = "text";
                newpass.type = "text";
            }
            else {
                passcon.type = "password";
                newpass.type = "password";
            }
        }

        var proview = document.getElementById("profile-view");
        var profilefull = document.getElementById("profile-full");
        proview.addEventListener("click", () => {
            prohide = document.getElementById("profile-hid");
            prohide.classList.remove("d-none");
        });
        proview.addEventListener("dblclick", () => {
            prohide = document.getElementById("profile-hid");
            prohide.classList.add("d-none");
        });
        var video = document.getElementById('Videocnt');
        var cmpbutton = document.getElementById('compbutton');
        video.addEventListener('ended', () => {
            // Enable the button when the video ends
            cmpbutton.disabled = false;
        });
        video.addEventListener('timeupdate', () => {
            // Check if the video is near the end
            if (video.currentTime >= video.duration - 3) { // You can adjust the threshold as needed
                // Disable the button if the video is dragged to the end
                cmpbutton.disabled = true;
            }
        });
    </script>
    <!-- script  bootstrap link-->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
        integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"
        integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"
        crossorigin="anonymous"></script>
    <!-- script  bootstrap link-->
</body>

</html>
""")

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
curs = dbconn.cursor()

newpassword = form.getvalue('newconpass')
oldpassword = form.getvalue('oldpass')
passchbtn = form.getvalue('passchbtn')

if passchbtn != None:
    fquery = ("""select id from user_details where id = '%s' and password = '%s'""" % (uid, oldpassword))
    curs.execute(fquery)
    getid = cur.fetchone()
    if getid != None:
        query = ("""UPDATE user_details SET password = '%s' WHERE id = '%s'""" % (newpassword, getid))
        curs.execute(query)
        print("""
            <script>
                window.location.href="UserDashboard.py?id=%s";
                var oldpass = document.forms['password_change']['oldpass'];
                oldpass.classList.add("is-valid");
                oldpass.classList.remove("is-invalid");
                alert("password is changed");
            </script>
        """ % uid)
    else:
        print("""
                    <script>
                            alert("Old Password is incorrect....");

                            $(document).ready(function(){
                                // Open the modal
                                $('#password_change_modal').modal('show');
                            });
                            var oldpass = document.forms['password_change']['oldpass'];
                            oldpass.classList.add("is-invalid");
                            oldpass.classList.remove("is-valid");
                    </script>               
                """)
dbconn.commit()
dbconn.close()
