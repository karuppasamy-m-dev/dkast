#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe

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
</head>

<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid pe-5">
            <a href="" class="navbar-brand"><img class="brand-logo" src="./Resources/images/logo.png" alt="project_logo"></a>
            <div class="d-flex align-items-center">
                <div class="admin-text d-flex align-items-center">
                    <h3><i class="fa-solid fa-circle-user pe-1" style="color: white;"></i>Admin</h3>
                </div>
                <div class="mx-2 hr"></div>
                <div class="logout-btn">
                    <a href="./Index.py">Logout<i class="fa-solid fa-right-from-bracket ps-2"></i></a>
                </div>
            </div>
        </div>
    </nav>
    <section class="admin-panel">
        <div class="nav-panel d-md-block d-none">
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
            <div class="container p-md-5 p-2">
                <div class="accordion">
                    <div class="accordion-item pb-2">
                        <div class="accordion-header">
                            <button class="w-100 btn btn-warning text-align-center" type="button"
                                data-bs-toggle="collapse" data-bs-target="#Accor-python">
                                <span class="btn-font">Python Staff'S</span>
                            </button>
                        </div>
                        <div class="accordion-collapse collapse" id="Accor-python" tabindex="-1">
                            <div class="accordion-body">
                                <div class="container py-5">
                                    <div class="card-parent">
                                        <div class="row">""")
import cgitb, cgi
import pymysql

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
conn = dbconn.cursor()
q = """select * from emp_details"""
conn.execute(q)
details = conn.fetchall()
for emp in details:
    eid = emp[1]
    ename = emp[2]
    eemailid = emp[3]
    enumber = emp[4]
    empphotoloc = "Resources/images/staff_images/" + emp[9]
    print("""
                                            <div class="col-xl-6 pb-md-4 pb-sm-4 pb-4">
                                                <div class="emp-card">
                                                    <div class="emp-card-img">
                                                        <img src="%s" alt=""
                                                            class="img-fluid card-img-css shadow">
                                                    </div>
                                                    <div class="emp-card-body">
                                                        <div class="card-cont">
                                                            <h6 class="d-flex justify-content-end small" id="empid">
                                                                %s</h6>
                                                            <h4>%s</h4>
                                                            <h6 class="d-flex"><i class="fa-solid fa-envelope-open-text pe-2"
                                                                    style="color: white;"></i>%s</h6>
                                                            <h6 class="d-flex"><i class="fa-solid fa-mobile-screen-button pe-2"
                                                                    style="color: white;"></i>%s</h6>
                                                            <span class="d-flex justify-content-end">
                                                                <button type="button" class="btn martop"
                                                                    data-bs-toggle="modal"
                                                                    data-bs-target="#empviewmodal">
                                                                    Click to More Details<span class="trans"><i
                                                                            class="fa-solid fa-angle-right ms-2"></i><i
                                                                            class="fa-solid fa-angle-right"></i></span>
                                                                </button>

                                                            </span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>""" % (empphotoloc, eid, ename, eemailid, enumber))
    dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
    conn = dbconn.cursor()
    qu = ("""select * from emp_details where EmpId = '%s' """ % eid)
    conn.execute(qu)
    edetails = conn.fetchall()
    for j in edetails:
        jid = j[1]
        jname = j[2]
        jmail = j[3]
        jnumber = j[4]
        jdob = j[5]
        jgender = j[6]
        jaddress = j[7]
        jphoto = j[9]
        jjphoto = "Resources/images/staff_images/" + jphoto

        print("""
            <div class="modal fade" id="empviewmodal" tabindex="-1"
                                                                    aria-hidden="true">
                                                                    <div class="modal-dialog modal-dialog-centered">
                                                                        <div class="modal-content">
                                                                            <div class="modal-body">
                                                                                <div class="px-md-4 pt-md-3 px-2">
                                                                                    <div class="row">
                                                                                        <div
                                                                                            class="col empviewmodal-cont">
                                                                                            <div
                                                                                                class="staff-images p-1">
                                                                                                <img src="%s"
                                                                                                    alt="" width="110px"
                                                                                                    height="130px">
                                                                                            </div>
                                                                                            <div class="mb-4">
                                                                                                <h4 class="emp-lbl">Employee Id</h4>
                                                                                                <h2
                                                                                                    class="emp-val ps-2">
                                                                                                    %s</h2>
                                                                                            </div>
                                                                                            <div class="mb-4">
                                                                                                <h4 class="emp-lbl">Name
                                                                                                </h4>
                                                                                                <h2
                                                                                                    class="emp-val ps-2">
                                                                                                    %s</h2>
                                                                                            </div>
                                                                                            <div class="mb-4">
                                                                                                <h4 class="emp-lbl">
                                                                                                    Email ID</h4>
                                                                                                <h2
                                                                                                    class="emp-val ps-2">
                                                                                                   %s
                                                                                                </h2>
                                                                                            </div>
                                                                                            <div class="row">
                                                                                                <div class="col mb-4 ">
                                                                                                    <h4 class="emp-lbl">
                                                                                                        Date
                                                                                                        of Birth</h4>
                                                                                                    <h2
                                                                                                        class="emp-val ps-2">
                                                                                                        %s</h2>
                                                                                                </div>
                                                                                                <div
                                                                                                    class="col mb-4 d-flex justify-content-center">
                                                                                                    <div>
                                                                                                        <h4
                                                                                                            class="emp-lbl">
                                                                                                            Gender</h4>
                                                                                                        <h2
                                                                                                            class="emp-val ps-2">
                                                                                                          %s
                                                                                                        </h2>
                                                                                                    </div>
                                                                                                </div>
                                                                                            </div>
                                                                                            <div class="mb-4">
                                                                                                <h4 class="emp-lbl">
                                                                                                    Address</h4>
                                                                                                <h2 class="emp-val ps-2"> %s </h2>
                                                                                            </div>
                                                                                            <div class="mb-2">
                                                                                                <h4 class="emp-lbl">
                                                                                                    Phone Number</h4>
                                                                                                <h2
                                                                                                    class="emp-val ps-2">
                                                                                                    +91 %s</h2>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="modal-footer  row">
                                                                                <div class="col w-100">
                                                                                    <button type="button"
                                                                                        class="btn btn-danger w-100"
                                                                                        data-bs-dismiss="modal">
                                                                                        close
                                                                                    </button>
                                                                                </div>
                                                                                <div class="col w-100">
                                                                                    <button type="button"
                                                                                        class="btn btn-info w-100">
                                                                                        Edit
                                                                                    </button>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
         """ % (jjphoto, jid, jname, jmail, jdob, jgender, jaddress, jnumber))
print("""
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="accordion-item pb-2">
                        <div class="accordion-header">
                            <button class="w-100 btn btn-info text-align-center" type="button" data-bs-toggle="collapse"
                                data-bs-target="#Accor-java">
                                <span class="btn-font">Java Staff'S</span>
                            </button>
                        </div>
                        <div class="accordion-collapse collapse" id="Accor-java">
                            <div class="accordion-body">
                                <div class="container py-5">
                                    <div class="card-parent">
                                        <div class="row">
                                            <div class="col-lg-6 pb-md-4 pb-sm-4 pb-4">
                                                <div class="emp-card">
                                                    <div class="emp-card-img">
                                                        <img src="./Resources/images/staff_images/janagaraj.jpeg" alt=""
                                                            class="img-fluid card-img-css">
                                                    </div>
                                                    <div class="emp-card-body">
                                                        <div class="card-cont">
                                                            <h4>Janagaraj M</h4>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6">
                                                <div class="emp-card">
                                                    <div class="emp-card-img">
                                                        <img src="./Resources/images/staff_images/janagaraj.jpeg" alt=""
                                                            class="img-fluid card-img-css">
                                                    </div>
                                                    <div class="emp-card-body">
                                                        <div class="card-cont">
                                                            <h4>Janagaraj M</h4>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
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