#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
import cgi,cgitb,pymysql
import os

print("content-type:text/html \r\n\r\n")

form = cgi.FieldStorage()
uid = form.getvalue('id')

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
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>   
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
                    </div>
                    <div class="profile" id="profile-full">
                        <div class="profile-hid d-none" id="profile-hid">
                            <div class="profile-in" id="profile-in">
                                <a href="./UserProfileEdit.py?id=%s"><i class="fa-solid fa-gear"
                                        style="color: #162133; font-size: 20px;"></i></a>""" % (uid, uid, uid, uid))
print(""" 
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
                <div class="container p-5">""")
cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

retqury = ("""select * from user_details where id = '%s'""" % uid)
cur.execute(retqury)
retdata = cur.fetchall()
for i in retdata:
    print("""                
                    <form action="" method="post" enctype="multipart/form-data" name="user_reg_form">
                        <div class="row">
                            <div class="col-md-3">
                                <div class="py-3 form-floating">
                                    <input type="text" name="us-id"
                                        class="form-control" id="UserId" value="%s" readonly />
                                    <label for="UserId" class="pt-4">User ID</label>
                                </div>
                            </div>
                            <div class="col-md-9">
                                <div class="py-3 form-floating">
                                    <input type="text" name="usname"
                                        class="form-control" id="UserName1" value="%s" required />
                                    <label for="UserName" class="pt-4">User Name</label>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="py-2 form-floating">
                                    <input type="date" name="usdob" class="form-control" id="UserDob" value="%s" required/>
                                    <label for="UserDob">DOB</label>
                                </div>
                            </div>""" % (i[1], i[2], i[4]))
    print("""
                            <div class="col-md-6">
                                <div class="py-2">
                                    <div class="">
                                        <label style="color: white;font-size: large;" class="form-label">Gender</label><br>
                                        <div class="px-5 d-flex justify-content-sm-evenly">
                                            <div class="">
                                                <input type="radio" name="usgen" value="Male" id="usmale"
                                                class="form-check-label" %s>
                                            <label for="usmale" class="form-check-label me-3"
                                                style="color: white; font-size: large;">Male</label>
                                            </div>
                                            <div class="">
                                                <input type="radio" name="usgen" value="Female" id="usfemale"
                                                class="form-check-label" %s>
                                            <label for="usfemale" class="form-check-label me-3"
                                                style="color: white;font-size: large;">Female</label>
                                            </div>
                                            <div class="div">
                                                <input type="radio" name="usgen" value="Others" id="usother"
                                                class="form-check-label" %s>
                                            <label for="usother" class="form-check-label me-2"
                                                style="color: white;font-size: large;">Other</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>""" % ('checked' if i[10] == 'Male' else '', 'checked' if i[10] == 'Female' else '', 'checked' if i[10] == 'Others' else ''))
    print("""
                        <div class="row">
                            <div class="col-md-6">
                                <div class="py-2 form-floating">
                                    <input type="number" name="usnumber" placeholder="Enter Number ..."
                                        class="form-control" id="UserNumber" value='%s' required />
                                    <label for="UserNumber">Contact Number</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="py-2 form-floating">
                                    <input type="email" name="us-email" placeholder="Enter Email id ..."
                                        class="form-control" id="UserEmail" value='%s' required />
                                    <label for="UserEmail">Email Id</label>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="py-2 form-floating">
                                    <input type="text" name="us-addres" placeholder="Enter Address ..."
                                        class="form-control" id="UserAddress" value="%s" required />
                                    <label for="UserAddress">Address</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="py-2 form-floating">
                                    <input type="text" name="us-pincode" placeholder="Enter Pincode ..."
                                        class="form-control" id="UserPincode" value="%s" required />
                                    <label for="UserPincode">Pincode</label>
                                </div>
                            </div>
                        </div>""" % (i[5], i[3], i[7], i[8]))
    print("""                        
                        <div class="row">
                            <div class="col-md-9">
                                <div class="py-2 form-floating">
                                    <select name="usprofession" id="UserProfession" class="form-control" required>
                                        <option>select Profession</option>
                                        <option value="Student" %s>Student</option>
                                        <option value="Employed" %s>Employed</option>
                                        <option value="UnEmployed" %s>UnEmployed</option>
                                        <option value="Self-Employed" %s>Self-Employed</option>
                                    </select>
                                    <label for="UserProfession">Profession</label>
                                </div>
                            </div>""" % ('selected' if i[6] == 'Student' else '',
                                         'selected' if i[6] == 'Employed' else '',
                                         'selected' if i[6] == 'UnEmployed' else '',
                                         'selected' if i[6] == 'Self-Employed' else '',))
    print("""                            
                            <div class="col-md-3">
                                <label for="UserImage" style="color: white;">Upload Your Image <span
                                        class="text-muted">(optional)</span></label>
                                <input type="file" name="usimage" 
                                    class="form-control" id="UserImage" required />
                            </div>
                        </div>
                        <div class="pt-3 row">
                            <div class="pb-2 d-flex justify-content-center">
                                <input type="submit" name="ussubmitbtn" class="btn btn-success py-2 px-5"
                                    value="Register" />
                            </div>
                        </div>
                    </form>""")
print("""    
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
                            <input type="password" name="newconpass" id="newconpass" class="form-control" oninput="return differFun()">
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
        
        function differFun(){
            if (passcon.value == newpass.value){
                newpass.classList.add("is-valid");
                passcon.classList.add("is-valid");
                newpass.classList.remove("is-invalid");
                passcon.classList.remove("is-invalid");
                return true;
            }
            if (passcon.value != newpass.value){
                newpass.classList.add("is-invalid");
                passcon.classList.add("is-invalid");
                newpass.classList.remove("is-valid");
                passcon.classList.remove("is-valid");
                return true;
            }
            if (passcon.length == 0 || newpass.length == 0){
                newpass.classList.remove("is-invalid");
                passcon.classList.remove("is-invalid");
                newpass.classList.remove("is-valid");
                passcon.classList.remove("is-valid");
                return true;
            }
        }
        
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
cur = dbconn.cursor()

newpassword = form.getvalue('newconpass')
oldpassword = form.getvalue('oldpass')
passchbtn = form.getvalue('passchbtn')

if passchbtn != None:
    fquery = ("""select id from user_details where id = '%s' and password = '%s'""" % (uid, oldpassword))
    cur.execute(fquery)
    getid = cur.fetchone()
    if getid != None:
        query = ("""UPDATE user_details SET password = '%s' WHERE id = '%s'""" % (newpassword, getid))
        cur.execute(query)
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

cgitb.enable()
dbconn1 = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
curs = dbconn1.cursor()

username = form.getvalue('usname')
userdob = form.getvalue('usdob')
usergender = form.getvalue('usgen')
usernumber = form.getvalue('usnumber')
useremail = form.getvalue('us-email')
useraddress = form.getvalue('us-addres')
userpincode = form.getvalue('us-pincode')
userprofession = form.getvalue('usprofession')
useditbtn = form.getvalue('ussubmitbtn')

if useditbtn != None:
    userimage = form['usimage']
    if userimage.filename:
        userimagefile = os.path.basename(userimage.filename)
        open("Resources/userpic/" + userimagefile, "wb").write(userimage.file.read())
        upquery = (""" UPDATE user_details SET username = '%s', useremail = '%s', userdob = '%s', usernumber = '%s', profession = '%s', address = '%s', pincode = '%s', usergender = '%s', profilepic = '%s' WHERE id = '%s' """ % (username, useremail, userdob, usernumber, userprofession, useraddress, userpincode, usergender, userimagefile, uid))
        curs.execute(upquery)
        if upquery:
            print("""
                    <script>
                        alert("your Details has been updated");
                        window.location.href="./UserDashboard.py?id=%s";
                    </script>
                    """ % uid)
        else:
            print("""
                    <script>
                        alert("error in your Details updation");
                        window.location.href="./UserProfileEdit.py?id=%s";
                    </script>
                    """ % uid)
    else:
        print("""
                <script>
                    alert("Error in update <br> check your image file ");
                    window.location.href="./UserProfileEdit.py?id=%s";
                </script>
                """ % uid)

dbconn1.commit()
dbconn1.close()
