#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
import pymysql
import cgi
import cgitb
from datetime import date

today = date.today()
year = today.year

form = cgi.FieldStorage()
pid = form.getvalue('id')

print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin_page</title>
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
        function moncalc(){
            var month = document.forms["Salary_calc_form"]["month"];
            var working = document.forms["Salary_calc_form"]["wdays"];
            var monthcheck = month.value;
            if (monthcheck == 'Jan'){
                working.value = "31";
            }
            if (monthcheck == 'Feb'){
                working.value = "28";
            }
            if (monthcheck == 'Mar'){
                working.value = "31";
            }
            if (monthcheck == 'April'){
                working.value = "30";
            }
            if (monthcheck == 'May'){
                working.value = "31";
            }
            if (monthcheck == 'June'){
                working.value = "30";
            }
            if (monthcheck == 'July'){
                working.value = "31";
            }
            if (monthcheck == 'Aug'){
                working.value = "31";
            }
            if (monthcheck == 'Sep'){
                working.value = "30";
            }
            if (monthcheck == 'Oct'){
                working.value = "31";
            }
            if (monthcheck == 'Nov'){
                working.value = "30";
            }
            if (monthcheck == 'Dec'){
                working.value = "31";
            }
        }
        function leave(){            
            var working = document.forms["Salary_calc_form"]["wdays"];
            var present = document.forms["Salary_calc_form"]["pdays"];
            var leave = document.forms["Salary_calc_form"]["ldays"];            
            var salary = document.forms["Salary_calc_form"]["salary"];
            var gross = document.forms["Salary_calc_form"]["gsalary"];

            var workingv = parseInt(working.value);
            var leavev = parseInt(leave.value);
            var presentv = workingv - leavev; 
            present.value  = presentv;
            
            var salaryv = parseInt(salary.value);
            var grossv = Math.round((salaryv * presentv)/workingv);
            gross.value = grossv;
        }
    </script>
</head>

<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid pe-5">
            <a href="" class="navbar-brand"><img class="brand-logo" src="./Resources/images/logo.png"
                    alt="project_logo"></a>
            <div class="d-flex align-items-center">
                <div class="admin-text d-flex align-items-center">
                    <h3><i class="fa-solid fa-circle-user pe-1" style="color: white;"></i>Admin</h3>
                </div>
                <div class="mx-2 hr"></div>
                <div class="logout-btn">
                    <a href="./index.py">Logout<i class="fa-solid fa-right-from-bracket ps-2"></i></a>
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
                            data-bs-target="#empdrop" aria-controls="empdrop">Employee Details <i
                                class="fa-solid fa-caret-down" style="color: white;"></i></h5>
                    </li>
                    <div class="collapse" id="empdrop">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpAdd.py">Add</a></li>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpView.py">View</a></li>
                        </ul>
                    </div>
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empleave">Employee Leave <i class="fa-solid fa-caret-down"
                                style="color: white;"></i>
                        </h5>

                    </li>
                    <div class="collapse" id="empleave">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./AdminLeaveView.py">View</a></li>
                        </ul>
                    </div>
                    <li class="mt-3">
                        <h5 class="w-100" type="button" data-bs-toggle="collapse" aria-expanded="false"
                            data-bs-target="#empsalary">Employee Salary <i class="fa-solid fa-caret-down"
                                style="color: white;"></i>
                        </h5>
                    </li>
                    <div class="collapse" id="empsalary">
                        <ul>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpSalary.py">Calculation</a></li>
                            <li class="mt-2"><a class="px-5" href="./AdminEmpSalaryView.py">View</a></li>
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
                <div class="border m-5 p-5">
                    <h4 class=" text-center heading">Salary Details</h4>
                    <form method="post" enctype="multipart/form-data" name="Salary_calc_form">""")
cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = """select * from emp_details where id = '%s'""" % pid
cur.execute(query)
data = cur.fetchall()
lev = 0
for i in data:
    empid = i[1]
    empname = i[2]
    empsalary = i[10]
    print("""
                        <div class="row mb-2">
                            <div class="col-sm-12 col-lg-3 p-2">
                                <label for="empid" class="form-label">Employee Id:</label>
                                <input type="text" class="form-control" name="Emp_id" id="empid" value="%s" readonly>
                            </div>
                            <div class="col-sm-12 col-lg-9 p-2">
                                <label for="empname" class="form-label">Employee Name</label>
                                <input type="text" id="empname" class="form-control" name="Emp_Name" value="%s"
                                    readonly>
                            </div>
                        </div>
                        <div class="row mb-2">
                            <div class="col-sm-12 col-lg-4 p-2">
                                <label for="year" class="form-label">Year</label>
                                <input type="text" id="year" class="form-control" name="year" value="%s" required>
                            </div>
                            <div class="col-sm-12 col-lg-4 p-2">
                                <label for="month" class="form-label">Month</label>
                                <select name="month" id="month" class="form-control" onchange="moncalc();leave();" required>
                                    <option>select month</option>
                                    <option value="Jan">Jan</option>
                                    <option value="Feb">Feb</option>
                                    <option value="Mar">Mar</option>
                                    <option value="April">April</option>
                                    <option value="May">May</option>
                                    <option value="June">June</option>
                                    <option value="July">July</option>
                                    <option value="Aug">Aug</option>
                                    <option value="Sep">Sep</option>
                                    <option value="Oct">Oct</option>
                                    <option value="Nov">Nov</option>
                                    <option value="Dec">Dec</option>
                                </select>
                            </div>
                            <div class="col-sm-12 col-lg-4 p-2">
                                <label for="salary" class="form-label">Salary</label>
                                <input type="text" name="salary" value="%s" id="salary" class="form-control" readonly>
                            </div>
                        </div>""" % (empid, empname, year, empsalary))
    print("""                        
                        <div class="row mb-2">                          
                            <div class="col-sm-12 col-lg-3 p-2">
                                <label for="wdays" class="form-label">Working Days</label>
                                <input type="text" id="wdays" class="form-control" name="wdays" required>
                            </div>
                            <div class="col-sm-12 col-lg-3 p-2">
                                <label for="pdays" class="form-label">Present Days</label>
                                <input type="text" id="pdays" class="form-control" name="pdays" required>
                            </div>""")
    dbconn.commit()
    dbconn.close()

    cgitb.enable()
    dbconn1 = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
    cur1 = dbconn1.cursor()

    qu1 = """select * from emp_leave_detailes where empid = '%s' && status = 'Approved' && paidornot = 'not'""" % empid
    cur1.execute(qu1)
    lev = cur1.fetchall()
    totleaveid = []
    totleavecount = []
    if lev:
        for j in lev:
            leaveid = j[0]
            totleaveid.append(leaveid)
            leavecount = j[7]
            totleavecount.append(leavecount)
        sum = 0
        for k in totleavecount:
            addsum = int(k)
            sum = sum + addsum
        # print(sum)
        print("""                            
                                <div class="col-sm-12 col-lg-3 p-2">
                                    <label for="ldays" class="form-label">Leave Days</label>
                                    <input type="text" class="form-control" name="ldays" value="%s" id="ldays" required>
                                </div>""" % sum)
    else:
        print("""                            
                                        <div class="col-sm-12 col-lg-3 p-2">
                                            <label for="ldays" class="form-label">Leave Days</label>
                                            <input type="text" class="form-control" name="ldays" value="%s" id="ldays" required>
                                        </div>""" % 0)
    dbconn1.commit()
    dbconn1.close()
print("""
                            <div class="col-sm-12 col-lg-3 p-2">
                                <label for="gsalary" class="form-label">Gross pay</label>
                                <input type="text" id="gsalary" class="form-control" name="gsalary" required>
                            </div>
                        </div>
                        <div class="row mt-lg-5">
                            <div class="col-lg-12 d-flex justify-content-center">
                                <input type="submit" name="Submit" value="Submit" class="btn add-btn px-4 py-2">
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
dbconn2 = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
curs2 = dbconn2.cursor()

epid = form.getvalue("Emp_id")
epyear = form.getvalue('year')
epmonth = form.getvalue('month')
epsalary = form.getvalue('salary')
epwdays = form.getvalue('wdays')
eppdays = form.getvalue('pdays')
epldays = form.getvalue('ldays')
epgrspay = form.getvalue('gsalary')
btn = form.getvalue('Submit')

if btn != None:
    inqur = ("""INSERT INTO emp_salary_details (empid, year, month, salary, workingdays, presentdays, leavedays, gross_salary, calcdate) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (epid, epyear, epmonth, epsalary, epwdays, eppdays, epldays, epgrspay, today))
    curs2.execute(inqur)
    if inqur:
        print("""
            <script>
                alert("Employee Salary Details Updated");
                location.href = "./AdminEmpSalaryView.py";
            </script>
        """)
        for m in totleaveid:
            inqur1 = """UPDATE emp_leave_detailes SET paidornot = 'PAID' WHERE id = '%s' """ % m
            curs2.execute(inqur1)
        # print("""
        #             <script>
        #                 alert("Employee Salary Details Updated");
        #                 location.href = "./AdminEmpSalaryCalc.py?id=%s";
        #             </script>
        #         """ % pid)
    else:
        print("""
            <script>
                alert("query Error in Employee Salary Details Update");
                location.href = "./AdminEmpSalaryCalc.py?id=%s";
            </script>
        """ % pid)
dbconn2.commit()
dbconn2.close()
