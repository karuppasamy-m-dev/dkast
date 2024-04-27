#!C:/Users/karup/AppData/Local/Programs/Python/Python311/python.exe
import pymysql
import cgi
import cgitb
import os
import smtplib
print("content-type:text/html \r\n\r\n")
cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

q = """select max(id) from emp_details"""
cur.execute(q)
re = cur.fetchone()

if re[0] != None:
    n = re[0]
else:
    n = 0

z = ""
if n < 9:
    z = "000"
elif 10 <= n <= 99:
    z = "00"
elif 100 <= n <= 999:
    z = "0"

empid = "EMP"+z+str(n+1)
dbconn.commit()
dbconn.close()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin_page</title>
    <link rel="stylesheet" href="./Resources/style.css">
    <!-- boostrap css -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <!-- fontawsome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid pe-5">
            <a href="" class="navbar-brand"><img class="brand-logo" src="./Resources/images/logo.png" alt="project_logo"></a>
            <div class="d-flex align-items-center">
                <div class="admin-text d-flex align-items-center">
                    <a href="./AdminDashboard.html"><i class="fa-solid fa-circle-user pe-1"
                            style="color: white;"></i>Admin</a>
                </div>
                <div class="mx-2 hr"></div>
                <div class="logout-btn">
                    <a href="./Index.py">Logout<i class="fa-solid fa-right-from-bracket ps-2"></i></a>
                </div>
            </div>
        </div>
    </nav>
    <section class="admin-panel">
        <div class="nav-panel">
            <div class="container">
                <ul class="nav-panel-ul">
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="true"
                            data-bs-target="#empdrop">Employee Details <i class="fa-solid fa-caret-down"
                                style="color: white;"></i></h5>

                    </li>
                    <div class="collapse" id="empdrop">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpAdd.py">Add</a></li>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpView.py">View</a></li>
                        </ul>
                    </div>
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empinvendrop" aria-controls="empinvendrop">Iventroy Details <i
                                class="fa-solid fa-caret-down" style="color: white;"></i></h5>
                    </li>
                    <div class="collapse" id="empinvendrop">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./AdminInventoryView.py">View</a></li>
                        </ul>
                    </div>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>
        </div>
        <div class="nav-content">
            <div class="container">
                <div class="form_entry p-5">
                    <form method="post" enctype="multipart/form-data" name="emp_entry_form" class="form-control">
                        <div class="row mb-2">
                            <div class="col-sm-12 col-lg-3 p-2">
                                <label for="empid" class="form-label">Employee Id:</label>""")
print("""
                                <input type="text" class="form-control" name="Emp_id" id="empid" value="%s" readonly>
                                 """ % empid)
print("""                   </div>
                            <div class="col-sm-12 col-lg-9 p-2">
                                <label for="empname" class="form-label">Employee Name</label>
                                <input type="text" id="empname" class="form-control" name="Emp_Name" required>
                            </div>
                        </div>
                        <div class="row mb-2">
                            <div class="col-lg-6 p-2">
                                <label for="empmail" class="form-label">Email Id</label>
                                <input type="email" class="form-control" id="empmail" name="Emp_Mailid" required>
                            </div>
                            <div class="col-lg-6 p-2">
                                <label for="empmob" class="form-label">Mobile Number</label>
                                <input type="number" class="form-control" name="Emp_Number" id="empmob" maxlength="10" required>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <div class="col-lg-6 p-2">
                                <div class="row mb-4">
                                    <div class="col-lg-12">
                                        <label for="empdob" class="form-label">Date of Birth</label>
                                        <input type="date" class="form-control" id="empdob" name="Emp_Dob">
                                    </div>
                                </div>
                                <div class="row">
                                    <label class="form-label">Gender</label>
                                    <div class="col-lg-12 px-2">
                                        <div class="row px-4">
                                            <div class="col-md-4 form-check ">
                                                <label for="emp_male" class="form-check-label">Male</label>
                                                <input type="radio" id="emp_male" name="Emp_Gender"
                                                    class="form-check-input" value="Male">
                                            </div>
                                            <div class="col-md-4 form-check">
                                                <label for="emp_female" class="form-check-label">Female</label>
                                                <input type="radio" id="emp_female" name="Emp_Gender"
                                                    class="form-check-input" value="Female">
                                            </div>
                                            <div class="col-md-4 form-check">
                                                <label for="emp_other" class="form-check-label">Others</label>
                                                <input type="radio" id="emp_other" name="Emp_Gender"
                                                    class="form-check-input" value="Others">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <label for="empadd" class="form-label">Address</label><br>
                                <textarea name="Emp_Address" id="empadd" rows="5" class="form-control"></textarea>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <div class="col-lg-6">
                                <div class="row mb-4">
                                    <div class="col-lg-12">
                                        <label for="pwd" class="form-label">Password</label>
                                        <div class="row">
                                            <div class="col-lg-11">
                                                <input type="text" class="form-control" name="Emp_Password" id="pwd"
                                                    required>
                                            </div>
                                            <div class="col-lg-1 d-flex align-items-center">
                                                <i class="fa-regular fa-circle-xmark" style="color: red;"
                                                    id="check-wr"></i>
                                                <i class="fa-regular fa-circle-check" style="color: #00f531;"
                                                    id="check-tick"></i>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-12">
                                        <label for="conpwd" class="form-label">Confirm Password</label>
                                        <div class="row">
                                            <div class="col-lg-11">
                                                <input type="text" class="form-control" name="Emp_con_Password"
                                                    id="conpwd" required oninput="return checktickfun()">
                                            </div>
                                            <div class="col-lg-1 d-flex align-items-center">
                                                <i class="fa-regular fa-circle-xmark" id="check-wr1"
                                                    style="color: red;"></i>
                                                <i class="fa-regular fa-circle-check" id="check-tick1"
                                                    style="color: #00f531;"></i>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="row mb-4">
                                    <div class="col-lg-12">
                                        <label for="empdept" class="form-label">Department</label>
                                        <select name="Emp_Depart" id="empdept" class="form-select" required>
                                            <option>Select Department</option>
                                            <option value="Python">Python Full Stack</option>
                                            <option value="Java">Java Full Stack</option>
                                            <option value="Cloud-Computing">Cloud Computing</option>
                                            <option value="Testing">Testing</option>
                                            <option value="Trainee">Trainee</option>
                                            <option value="Freelancer">Freelancing</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-12">
                                        <label for="empsalary" class="form-label">Salary</label>
                                        <input type="number" class="form-control" name="Emp_Salary" id="empsalary"
                                            required>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="row mb-4">
                            <div class="col">
                                <label for="image_upload" class="form-label">Upload Your Image</label>
                                <input type="file" class="form-control" name="Emp_Image" id="image_upload" required>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <div class="col-lg-12 d-flex justify-content-center">
                                <input type="submit" name="Add" value="Add" class="btn add-btn px-4 py-2">
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
    <footer>
        <div class="container">
            <div class="footer py-5">
                <div class="row">
                    <div class="col-sm-12 col-md-12 col-lg-4">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="brand">
                                    <a href="#"><span style="color: #50c2ff; font-size: 32px;">Dk</span>ast</a>
                                    <p class="brand-content ps-2 pt-2">
                                        Nine out of ten doctors recommend Dkasts over competing brands. Come inside, see
                                        for
                                        yourself, and massively level up your development skills in the process.
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="row pt-2">
                            <div class="col-md-12 pe-5">
                                <ul class="d-flex justify-content-start rm-p">
                                    <li><i class="fa-brands fa-facebook"
                                            style="font-size: 28px; color: white; opacity: 100%;"></i></li>
                                    <li><i class="fa-brands fa-twitter"
                                            style="font-size: 28px; color: white; opacity: 100%;"></i></li>
                                    <li><i class="fa-brands fa-instagram"
                                            style="font-size: 28px; color: white; opacity: 100%;"></i></li>
                                    <li><i class="fa-brands fa-linkedin"
                                            style="font-size: 28px; color: white; opacity: 100%;"></i></li>
                                    <li><i class="fa-brands fa-square-pinterest"
                                            style="font-size: 28px; color: white; opacity: 100%;"></i></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-12 col-lg-4 pt-4 px-4">
                        <div class="row">
                            <div class="col-sm-6 col-6">
                                <ul>
                                    <h3>Learn</h3>
                                    <li>Sign Up</li>
                                    <li>Sign In</li>
                                    <li>Pricings</li>
                                    <li>Topics</li>
                                </ul>
                            </div>
                            <div class="col-sm-6 col-6">
                                <ul>
                                    <h3>Extras</h3>
                                    <li>About Us</li>
                                    <li>Career</li>
                                    <li>Contact Us</li>
                                    <li>FAQ</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-12 col-lg-4 pt-4 d-md-flex gap-md-5 d-lg-block">
                        <div class="row">
                            <div class="col-sm-12">
                                <ul>
                                    <h3>Address</h3>
                                    <li>65/1, Tatabad, 7th Street, Dr Rajendra <br> Prasad Rd, near BEA,<br> Coimbatore,
                                        Tamil Nadu 641012</li>
                                    <li><i class="fa-solid fa-phone pt-3 pe-2"
                                            style="color: white; opacity: 100%;"></i><a href="tel:+919159779111">+91
                                            91597 79111</a></li>
                                    <li><i class="fa-solid fa-envelope pe-2" style="color: white; opacity: 100%;"></i><a
                                            href="mailto:enquiry@indrainstitute.com">enquiry&commat;indrainstitute.com</a>
                                    </li>
                                    <li><i class="fa-solid fa-envelope pe-2" style="color: white; opacity: 100%;"></i><a
                                            href="mailto:info@indrainstitute.com">info&commat;indrainstitute.com</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 px-4">
                                <iframe
                                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62655.04695368239!2d76.92068064312214!3d11.043092859270688!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba858f8b62adeeb%3A0xd6355321df881728!2sIIE-BEST%20DATASCIENCE%7CMACHINE%20LEARNING%7CCCNA%20TRAINING%7CETHICAL%20HACKING%7CAWS%7CLINUX%7CSELENIUM%20TESTING%7CFULL%20STACK%20PYTHON%7CJAVA%7CAZURE!5e0!3m2!1sen!2sin!4v1711606280322!5m2!1sen!2sin"
                                    width="100%" height="200" style="border:0;" allowfullscreen="" loading="lazy"
                                    referrerpolicy="no-referrer-when-downgrade"></iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <hr class="hrline">
        <div class="container-fluid cpyrght px-5">
            <div class="">
                <p>Copyrights &copy; 2024 Dkast</p>
                <p>its was developed by <span style="font-size: medium;">JK Techiezz..</span></p>
            </div>
        </div>
    </footer>
    <script>
        checkwr = document.getElementById("check-wr");
        checkwr1 = document.getElementById("check-wr1");
        checkwr.style.display = "None";
        checkwr1.style.display = "None";
        checktick = document.getElementById("check-tick");
        checktick.style.display = "None";
        checktick1 = document.getElementById("check-tick1");
        checktick1.style.display = "None";
        function checktickfun() {
            password = document.forms["emp_entry_form"]["Emp_Password"];
            conpass = document.forms["emp_entry_form"]["Emp_con_Password"];

            if (password.value == conpass.value) {
                checktick.style.display = "block";
                checktick1.style.display = "block";
                checkwr.style.display = "None";
                checkwr1.style.display = "None";
                return true;
            }
            else {
                checkwr.style.display = "block";
                checkwr1.style.display = "block";
                checktick.style.display = "None";
                checktick1.style.display = "None";
                return false;
            }

        }
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
form = cgi.FieldStorage()
eid = form.getvalue("Emp_id")
empname = form.getvalue("Emp_Name")
empemail = form.getvalue("Emp_Mailid")
empnumber = form.getvalue("Emp_Number")
empdob = form.getvalue("Emp_Dob")
empgender = form.getvalue("Emp_Gender")
empaddress = form.getvalue("Emp_Address")
emppwd = form.getvalue("Emp_con_Password")
empdepart = form.getvalue("Emp_Depart")
empsalary = form.getvalue("Emp_Salary")
submitbtn = form.getvalue("Add")

if submitbtn != None:
    empimage = form["Emp_Image"]
    if empimage.filename:
        empimgname = os.path.basename(empimage.filename)
        open("Resources/images/staff_images/" + empimgname, "wb").write(empimage.file.read())
        inqu = ("""INSERT INTO emp_details (EmpId, EmpName, EmpMailId, EmpNumber, Empdob, EmpGender, EmpAddress, EmpPwd, EmpDepart, EmpSalary, EmpImage) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (eid, empname, empemail, empnumber, empdob, empgender, empaddress, emppwd, empdepart, empsalary, empimgname))
        cur.execute(inqu)
        print("""
            <script>
                alert("Employee Details Added");
            </script>
            """)
        re = ""
        empid = ""
        fromaddr = "karuppasamy.mk.2024@gmail.com"
        password = "ekkilawteoijhjie"
        toaddr = empemail
        subject = "Form Dkast techiezz Learning site"
        body = """I am Karuppasamy form Dkast techiezz Learning site, we are added your profile in our site. you can login our site
            by using User Name: %s and your Password: %s""" % (empname, emppwd)
        msg = """Subject:{}\n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()
        print("""
                <script>
                    alert("Employee Details Sented");
                    window.location.href="./AdminEmpAdd.py";
                </script>
                """)

dbconn.commit()
dbconn.close()
