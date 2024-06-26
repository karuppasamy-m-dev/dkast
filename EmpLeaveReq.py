#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

form = cgi.FieldStorage()
pid = form.getvalue('id')

cgitb.enable()
dbconn = pymysql.connect(host="localhost",user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query1 = """select * from emp_details where id = '%s' """ % pid
cur.execute(query1)
data = cur.fetchall()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dkast-Emp</title>
    <link rel="stylesheet" href="./Resources/style.css">
    <link rel="shortcut icon" href="./Resources/images/logo.png" type="image/x-icon">
    <!-- boostrap css -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <!-- fontawsome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script>
    function dateFun() {
        // Function logic here
        console.log("dateFun() called");
        var frdate = document.forms['leavereq_form']['fromdate'];
        var endate = document.forms['leavereq_form']['todate'];
        var reasonoption = document.forms['leavereq_form']['reason'];
        var cdays = document.forms['leavereq_form']['cdate'];
        var hidecolumn = document.getElementById("hidecol");
        var daycount = new Date(endate.value) - new Date(frdate.value);
        
        var resultcount = daycount / (60 * 60 * 24 * 1000);
        console.log(resultcount);
        cdays.value = resultcount;
        countofdays = cdays.value;
        if (countofdays >= 4) {
            alert("You are requesting more than 4 days. Please confirm the dates and mention the reason.");
            reasonoption.value = "PL";
            hidecolumn.classList.remove("d-none");
        }
        return countofdays;
    }

    function dispFun() {
        // Function logic here
        var reasonoption = document.forms['leavereq_form']['reason'];
        var hidecolumn = document.getElementById("hidecol");
        if (reasonoption.value !== "CL") {
            return hidecolumn.classList.remove("d-none");
        } else {
            return hidecolumn.classList.add("d-none");
        }
    }
</script>

</head>

<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid pe-5">
            <a href="" class="navbar-brand"><img src="./Resources/images/logo.png" alt="project_logo"
                    class="brand-logo"></a>
            <div class="d-flex align-items-center">
                <div class="admin-text d-flex align-items-center">""")
empid = ""
empname = ""
for i in data:
    empid = i[1]
    empname = i[2]
    image = "./Resources/images/staff_images/" + i[11]
    print("""
                    <a href="./EmpDashboard.py?id=%s"><i class="fa-solid fa-circle-user pe-1" style="color: white;"></i>
                        %s</a>""" % (i[0],empname))
    print("""
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
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empdrop">Inventory Details <i class="fa-solid fa-caret-down"
                                style="color: white;"></i></h5>

                    </li>
                    <div class="collapse" id="empdrop">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./EmpInventoryAdd.py?id=%s">Add</a></li>
                            <li class="mt-2"><a class="px-5" href="./EmpInventoryView.py?id=%s">View</a></li>

                        </ul>
                    </div>
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empleave">Leave <i class="fa-solid fa-caret-down"
                                style="color: white;"></i>
                        </h5>

                    </li>
                    <div class="collapse" id="empleave">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./EmpLeaveReq.py?id=%s">Request</a></li>
                            <li class="mt-2"><a class="px-5" href="./EmpLeaveView.py?id=%s">View</a></li>
                        </ul>
                    </div>
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empsalary">Salary <i class="fa-solid fa-caret-down"
                                style="color: white;"></i>
                        </h5>

                    </li>
                    <div class="collapse" id="empsalary">
                        <ul>                            
                            <li class="mt-2"><a class="px-5" href="./EmpSalaryView.py?id=%s">View</a></li>
                        </ul>
                    </div>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>
        </div>
        <div class="nav-content">
            <div class="container">
                <div class="w-100 d-flex justify-content-end">
                    <img src="%s" class="img-fluid border p-2 " width="100px" height="100px">
                </div>""" % (pid, pid, pid, pid, pid, image))
print("""           
                <div class="w-100 p-5 border m-2">
                    <h3 class="mb-4">Leave Request</h3>
                    <form name="leavereq_form" method="post" enctype="multipart/form-data">
                        <div class="row mb-3">
                            <div class="col-sm-6">
                                <label for="frmdate" class="form-label">From Date</label>
                                <input type="date" class="form-control" id="frmdate" name="fromdate">
                            </div>
                            <div class="col-sm-5">
                                <label for="tdate" class="form-label">To Date</label>
                                <input type="date" class="form-control" id="tdate" name="todate" oninput="return dateFun()">

                            </div>
                            <div class="col-sm-1">
                                <label for="cdate" class="form-label">Days</label>
                                <input type="text" class="form-control" id="cdate" placeholder="0" name="cdate" readonly>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-sm-6">
                                <label for="reason" class="form-label">Reason</label>
                                <select name="reason" id="reason" class="form-control" oninput="return dispFun()">
                                    <option>Select your leave</option>
                                    <option value="CL">Casual Leave</option>
                                    <option value="SL">Sick Leave</option>
                                    <option value="PL">Personal Leave</option>
                                </select>
                            </div>
                            <div class="col-sm-6">
                                <div class="d-none" id="hidecol">
                                    <label for="otherreason" class="form-label">Reason</label>
                                    <input type="text" class="form-control" id="otherreason" name="otherreason"
                                        >
                                </div>
                            </div>
                        </div>
                        <!--
                        <div class="row">
                            <div class="col-sm d-flex align-items-center">
                                <label for="avilleave">Available Leaves on this Month:</label>
                                <input type="text" name="leaveavil" class="form-control w-25 ms-2" id="avilleave">
                            </div>
                        </div>
                        -->                                                
                        <div class="row pt-3">
                            <div class="col text-center">
                                <input type="submit" name="Request" value="Request" class="btn add-btn px-4 py-2">
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
            <div>
                <p>Copyrights &copy; 2024 Dkast</p>
                <p>its was developed by <span style="font-size: medium;">JK Techiezz..</span></p>
            </div>
        </div>
    </footer>
    <script>        
        var lcount = document.forms['leavereq_form']['leaveavil'];        
        function dateFun(){
            var frdate = document.forms['leavereq_form']['fromdate'];
            var endate = document.forms['leavereq_form']['todate'];
            var reasonoption = document.forms['leavereq_form']['reason'];
            var cdays = document.forms['leavereq_form']['cdate'];
            var hidecolumn = document.getElementById("hidecol");
            var daycount = new Date(endate.value) - new Date(frdate.value);
            
            var resultcount = daycount / (60 * 60 * 24 * 1000);
            console.log(resultcount);
            cdays.value = resultcount;
            countofdays = cdays.value;
            if (countofdays >= 4) {
                alert("You Request more then 4 days... confirm that date and mention that reason !!! \n that will under personal leave....");
                reasonoption.value = "PL";
                hidecolumn.classList.remove("d-none");
            }
            return countofdays;
        }

        function dispFun(){
            var reasonoption = document.forms['leavereq_form']['reason'];
            var hidecolumn = document.getElementById("hidecol");
            if (reasonoption.value != "CL") {
                return hidecolumn.classList.remove("d-none");
            }
            else {
                return hidecolumn.classList.add("d-none");
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
dbconn.commit()
dbconn.close()


cgitb.enable()
dbconn1 = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
curs = dbconn1.cursor()

id = empid
name = empname
formdate = form.getvalue('fromdate')
todate = form.getvalue('todate')
dayscount = form.getvalue('cdate')
letype = form.getvalue('reason')
reasontxt = form.getvalue('otherreason')
availleave = form.getvalue('leaveavail')
submitbtn = form.getvalue('Request')

if submitbtn != None:
    query2 = """ INSERT INTO emp_leave_detailes(empid, empname, reasontype, reason, fromleave, toleave, dayscount, status, paidornot) VALUES( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 'not')""" % (id, name, letype, "Casual Leave" if letype == 'CL'else reasontxt, formdate, todate, dayscount, 'Waiting List')
    curs.execute(query2)
    if query2:
        print("""
        <script>
            alert("Leave Request Sented to Admin");
            window.location.href="./EmpLeaveView.py?id=%s";
        </script>
        """ % pid)
    else:
        print("""
        <script>
            alert("Error to sent");
        window.location.href="./EmpLeaveReq.py?id=%s";
        </script>
        """ % pid)
dbconn1.commit()
dbconn1.close()
