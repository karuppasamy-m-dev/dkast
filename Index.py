#!C:/Users/karup/AppData/Local/Programs/Python/Python311/python.exe
import pymysql
import cgi,cgitb

print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dkast</title>
    <link rel="stylesheet" href="./Resources/style.css">
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
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid ">
            <button type="button" class="navbar-toggler" data-bs-target="#navbar-in" data-bs-toggle="collapse"
                aria-expanded="false" aria-controls="navbar-in">
                <i class="fa-regular fa-circle-user" style="color: #ffffff;"></i>
            </button>
            <a href="./Index.py" class="navbar-brand d-flex">
                <img class="brand-logo" src="./Resources/images/logo.png" alt="project_logo">
                <h1><span style="font-size: 32px;">Dk</span>ast...</h1>
            </a>
            <div class="collapse navbar-collapse d-lg-flex justify-content-end" id="navbar-in">
                <div class="navbar-nav gap30px">
                    <!-- <div class="search">
                                            <i class="fa-solid fa-magnifying-glass" style="color: #ffffff;"></i>
                                        </div> -->
                    <div class="nav-item"><button class="signin btnbg" type="button" data-bs-target="#signinbtn"
                            data-bs-toggle="modal">Sign In</button>
                        <div class="modal fade" id="signinbtn" aria-hidden="true" tabindex="-1">
                            <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content pt-5">
                                    <div class="modal-body p-4">
                                        <form method="post" name="signin_form" class="form_design p-4">
                                            <div class="d-flex justify-content-center text-center pb-3">
                                                <div>
                                                    <img src="./Resources/images/logo.png" alt="" width="80px">
                                                    <h1 class="mt-2">Sign In</h1>
                                                </div>
                                            </div>
                                            <div class="w-100 py-3 form-floating">
                                                <input type="text" name="u-name" placeholder="Enter User Name ..."
                                                    class="form-control" id="UserName1">
                                                <label for="UserName" class="pt-4">User Name</label>
                                            </div>
                                            <div class="w-100 py-2 form-floating">
                                                <input type="password" name="u-pass" placeholder="Enter Password ..."
                                                    class="form-control" id="UserPass1">
                                                <label for="UserPass">Password</label>
                                            </div>
                                            <div class="w-100 py-2 form-check">
                                                <input type="checkbox" name="showpass" id="showpass1"
                                                    class="form-check-input">
                                                <label for="showpass1" class="form-check-label">Show Password</label>
                                            </div>
                                            <div class="p-2 acc-links d-flex justify-content-end">
                                                <a href="#" class="forgetpass">Forget Password</a><br>
                                            </div>
                                            <div class="pt-2">
                                                <div class="pb-2 w-100">
                                                    <input type="submit" class="signinbtn w-100" value="Sign In">
                                                </div>
                                                <div class="d-flex justify-content-center acc-links p-2">
                                                    <a href="#" class="newacc">Register For
                                                        New Account</a>
                                                </div>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="nav-item"><button class="register btnbg">Get Started For Free</button></div>
                </div>
            </div>
        </div>
    </nav>
    <section class="banner-section">

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
                                    <li><a id="stlogbt" type="button" data-bs-target="#stafflogin" data-bs-toggle="modal">Staff login</a></li>                                  
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
    <div class="modal fade" id="stafflogin" aria-hidden="true" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content pt-5">
                <div class="modal-body p-4">
                    <form method="post" name="stafflogin_form" class="form_design p-4">
                        <div class="d-flex justify-content-center text-center pb-3">
                            <div>
                                <img src="./Resources/images/logo.png" alt="" width="80px">
                                <h1 class="mt-2">Sign In</h1>
                            </div>
                        </div>
                        <div class="w-100 py-3 form-floating">
                            <input type="text" name="stname" placeholder="Enter User Name ..." class="form-control"
                                id="UserName" required>
                            <label for="UserName" class="pt-4">User Name</label>
                        </div>
                        <div class="w-100 py-2 form-floating">
                            <input type="password" name="stpass" placeholder="Enter Password ..." class="form-control"
                                id="UserPass" required>
                            <label for="UserPass">Password</label>
                        </div>
                        <div class="w-100 py-2 form-check">
                            <input type="checkbox" name="showpass" id="showpass" class="form-check-input" >
                            <label for="showpass" class="form-check-label">Show Password</label>
                        </div>
                        <div class="p-2 acc-links d-flex justify-content-end">
                            <a href="#" class="forgetpass">Forget Password</a><br>
                        </div>
                        <div class="pt-2">
                            <div class="pb-2 w-100">
                                <input type="submit" name="stlogin" class="signinbtn w-100" value="Sign In">
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- script  bootstrap link-->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
        integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"
        integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"
        crossorigin="anonymous"></script>
 

    <!-- script  bootstrap link-->
    <script>
        var upass, upass1;
        var checkbtn, checkbtn1;
        stpass = document.forms['stafflogin_form']['stpass'];
        checkbtn = document.forms['stafflogin_form']['showpass'];
        checkbtn.onclick = function () {
            if (this.checked) {
                stpass.type = "text";
            }
            else {
                stpass.type = "password";
            }
        };
        upass1 = document.forms['signin_form']['u-pass'];
        checkbtn1 = document.forms['signin_form']['showpass'];
        checkbtn1.onclick = function () {
            if (this.checked) {
                upass1.type = "text";
            }
            else {
                upass1.type = "password";
            }
        };
        staname = document.forms['stafflogin_form']['stname'];
        stapass = document.forms['stafflogin_form']['stpass'];

    </script>""")

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()
form = cgi.FieldStorage()

uname = form.getvalue("stname")
upass = form.getvalue("stpass")
stloginbtn = form.getvalue("stlogin")

if stloginbtn != None:
    try:
        getid = None
        if uname == "jaga" and upass == '12345':
            print("""
                   <script>
                       staname.classList.remove("is-invalid");
                       stapass.classList.remove("is-invalid");
                       staname.value = '';
                       stapass.value = '';
                       alert("Login Successfully... welcome back !!!");                
                       location.href="./AdminDashboard.html";
                   </script>
               """)
        elif uname != None and upass != None:
            fquery = ("""select id from emp_details where EmpMailId = '%s' and EmpPwd = '%s'""" % (uname, upass))
            cur.execute(fquery)
            getid = cur.fetchone()
            dbconn.commit()
            dbconn.close()
            if getid != None:
                print("""
                    <script>
                        alert("login Successfully");
                        location.href="./EmpDashboard.py?id=%s";
                    </script>
                    """ % getid)
                getid = None

            else:
                print("""
                 <script>
                        alert("EmailId and Password is incorrect....");
                        $(document).ready(function(){
                            // Open the modal
                            $('#stafflogin').modal('show');
                        });
                </script>               
            """)
    except Exception as e:
        print("""
             <script>
                alert("Error occured:%s");
            </script>
        """ % e)
print("""
    </body>
</html>
""")
