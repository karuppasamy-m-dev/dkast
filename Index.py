#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
import smtplib

print("content-type:text/html \r\n\r\n")

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
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid ">
            <button type="button" class="navbar-toggler" data-bs-target="#navbar-in" data-bs-toggle="collapse"
                aria-expanded="false" aria-controls="navbar-in">
                <i class="fa-regular fa-circle-user" style="color: #ffffff;"></i>
            </button>
            <div>
                <a href="./Index.py" class="navbar-brand d-flex align-items-center">
                <img class="brand-logo" src="./Resources/images/logo.png" alt="project_logo"/>
                <h1 style="margin-bottom: 0">
                <span style="font-size: 32px">Dk</span>ast...</h1>
                </a>
            </div>
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
                                                <input type="email" name="u-name" placeholder="Enter User Name ..."
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
                                                    <input type="submit" name="usersignin" class="signinbtn w-100" value="Sign In">
                                                </div>
                                                <div class="d-flex justify-content-center acc-links p-2">
                                                    <a class="newacc" type="button" data-bs-toggle="modal" data-bs-target="#userregform">Register For New Account</a>
                                                </div>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="nav-item">
                        <button class="register btnbg" type="button" data-bs-toggle="modal" data-bs-target="#userregform">
                        Get Started For Free </button>
                    </div>
                    <div class="modal fade" id="userregform" aria-hidden="true" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content pt-4">
                <div class="modal-body p-5">
                  <form action="" method="post" enctype="multipart/form-data" name="user_reg_form">
                    <div class="d-flex justify-content-center text-center pb-3">
                      <div>
                        <img src="./Resources/images/logo.png" alt="" width="80px" />
                        <h1 class="mt-2">Register</h1>
                      </div>
                    </div>
                    <div class="w-100 py-3 form-floating">
                      <input type="text" name="us-name" placeholder="Enter User Name ..." class="form-control"
                        id="UserName1" required />
                      <label for="UserName" class="pt-4">User Name</label>
                    </div>                    
                    <div class="w-100 py-2 form-floating">
                      <input type="date" name="us-dob" class="form-control"
                        id="UserDob" required />
                      <label for="UserDob">DOB</label>
                    </div>
                    <div class="w-100 py-2 form-floating">
                      <input type="number" name="us-number" placeholder="Enter Number ..." class="form-control"
                        id="UserNumber" required />
                      <label for="UserNumber">Contact Number</label>
                    </div>
                    <div class="w-100 py-2 form-floating">
                      <input type="text" name="us-addres" placeholder="Enter Address ..." class="form-control"
                        id="UserAddress" required />
                      <label for="UserAddress">Address</label>
                    </div>
                    <div class="w-100 py-2 form-floating">
                      <input type="text" name="us-pincode" placeholder="Enter Pincode ..." class="form-control"
                        id="UserPincode" required />
                      <label for="UserPincode">Pincode</label>
                    </div>
                    <div class="w-100 py-2 form-floating">                      
                      <select name="us-profession" id="UserProfession" class="form-control" required>
                        <option>select Profession</option>
                        <option value="Student">Student</option>
                        <option value="Employed">Employed</option>
                        <option value="UnEmployed">UnEmployed</option>
                        <option value="Self-Employed">Self-Employed</option>
                      </select>
                      <label for="UserProfession">Profession</label>
                    </div>
                    <div class="w-100 py-2 form-floating">
                      <input type="email" name="us-email" placeholder="Enter Email id ..." class="form-control"
                        id="UserEmail" required />
                      <label for="UserEmail">Email Id</label>
                    </div>
                    <div>
                      <p class="text-muted">(password will sent to this email...)</p>
                    </div>
                    <div class="pt-3">
                      <div class="pb-2 w-100">
                        <input type="submit" name="us-submitbtn" class="signinbtn w-100 py-2" value="Register" />
                      </div>                      
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
                </div>
            </div>
        </div>
    </nav>
    <section>
      <div class="banner">
        <div class="container py-5">
          <div class="banner-parent d-flex">
            <div class="banner-txt w-100">
              <h1>
                Your Path to <br />
                Develop Your'Self <br />
              </h1>
              <span class="">Starts Here...</span>
            </div>
            <div class="backimg">
              <img
                class="img-fluid"
                src="./Resources/images/home-banner-illustration.svg"
                alt=""
                width="620px"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="course py-5">
        <div class="container">
            <div class="CC-Head mt-5">
                <div class="w-75">
                    <h3>A Stream of Endless Knowledge.</h3>
                    <p>
                        We're kinda like Netflix, but for developers! Push your
                        programming skills to the next level, through expert screencasts
                        on many Programmimg Language and so much more.
                    </p>
                </div>
            </div>
            <div class="CC-Part">
                <ul class="CC-parthead py-3 d-flex">
                    <li><button onclick="alldispFun()">All Topics</button></li>
                    <li><button onclick="langdispFun()">Language</button></li>
                    <li><button onclick="cloudispFun()">Cloud Based</button></li>
                    <li><button onclick="framdispFun()">FrameWorks</button></li>
                    <li><button onclick="dbdispFun()">Database</button></li>
                    <li><button onclick="testdispFun()">Testing</button></li>
                    <li><button onclick="scriptdispFun()">Script Language</button></li>
                </ul>
                <ul class="CC-partContent row">

                    <li class="cloud col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=aws">
                            <img src="./Resources/images/logos/aws-cloud.WEBP" alt="aws" />
                            <h3>AWS Cloud Service</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=cpro">
                            <img src="./Resources/images/logos/c-language.WEBP" alt="C-programe" />
                            <h3>C Language</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=cpp">
                            <img src="./Resources/images/logos/c.WEBP" alt="cpp" />
                            <h3>C++ Language</h3>
                        </a>
                    </li>
                    <li class="cloud col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=cloudcomputing">
                            <img src="./Resources/images/logos/cloudcomputing.WEBP" alt="cloudcomputing" />
                            <h3>Cloud Computing</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=csharp">
                            <img src="./Resources/images/logos/CSharp-Language.WEBP" alt="CSharp-Language" />
                            <h3>C# Language</h3>
                        </a>
                    </li>
                    <li class="scriptl col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=css">
                            <img src="./Resources/images/logos/css.WEBP" alt="CSS" />
                            <h3>CSS</h3>
                        </a>
                    </li>
                    <li class="FrameWorks col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=django">
                            <img src="./Resources/images/logos/django-framewrok.WEBP" alt="Django-framewrok" />
                            <h3>Django</h3>
                        </a>
                    </li>
                    <li class="scriptl col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=html">
                            <img src="./Resources/images/logos/html.WEBP" alt="HTML" />
                            <h3>HTML</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=java">
                            <img src="./Resources/images/logos/Java-language.WEBP" alt="Java" />
                            <h3>Java</h3>
                        </a>
                    </li>
                    <li class="scriptl col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=javascript">
                            <img src="./Resources/images/logos/JS-language.WEBP" alt="javascript" />
                            <h3>JavaScript</h3>
                        </a>
                    </li>
                    <li class="Testing col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=katalon">
                            <img src="./Resources/images/logos/katalon-testing.WEBP" alt="katalon-testing" />
                            <h3>Katalon</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=kotlin">
                            <img src="./Resources/images/logos/kotlin-language.WEBP" alt="Kotlin" />
                            <h3>Kotlin</h3>
                        </a>
                    </li>
                    <li class="FrameWorks col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=laravel">
                            <img src="./Resources/images/logos/laravel-framework.WEBP" alt="laravel-framework" />
                            <h3>Laravel</h3>
                        </a>
                    </li>
                    <li class="Database col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=mysql">
                            <img src="./Resources/images/logos/Mysql_logo.WEBP" alt="Mysql_logo" />
                            <h3>Mysql</h3>
                        </a>
                    </li>
                    <li class="FrameWorks col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=nodejs">
                            <img src="./Resources/images/logos/nodejs.WEBP" alt="nodejs" />
                            <h3>Node Js</h3>
                        </a>
                    </li>
                    <li class="Database col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=oracle">
                            <img src="./Resources/images/logos/Oracle-db.WEBP" alt="Oracle-db" />
                            <h3>Oracle</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=php">
                            <img src="./Resources/images/logos/PHP-language.WEBP" alt="PHP-language" />
                            <h3>PHP</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=python">
                            <img src="./Resources/images/logos/Python-language.WEBP" alt="Python-language" />
                            <h3>Python</h3>
                        </a>
                    </li>
                    <li class="Language col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=rprogram">
                            <img src="./Resources/images/logos/R-language.WEBP" alt="R-language" />
                            <h3>R Programmimg</h3>
                        </a>
                    </li>
                    <li class="FrameWorks col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=reactjs">
                            <img src="./Resources/images/logos/react-framework.webp" alt="react-framework" />
                            <h3>React Js</h3>
                        </a>
                    </li>
                    <li class="Testing col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=selenium">
                            <img src="./Resources/images/logos/selinium.WEBP" alt="selenium" />
                            <h3>Selenium</h3>
                        </a>
                    </li>
                    <li class="Testing col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=testrail">
                            <img src="./Resources/images/logos/TestRail-testing.WEBP" alt="TestRail-testing" />
                            <h3>TestRail</h3>
                        </a>
                    </li>
                    <li class="scriptl col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=typescript">
                            <img src="./Resources/images/logos/TypeScript-language.WEBP" alt="TypeScript-language" />
                            <h3>TypeScript</h3>
                        </a>
                    </li>
                    <li class="FrameWorks col-lg-3 col-sm-6 col-md-4 my-2">
                        <a href="./CourseDetails.py?course=vuejs">
                            <img src="./Resources/images/logos/vue.WEBP" alt="vuejs" />
                            <h3>Vue Js</h3>
                        </a>
                    </li>
                </ul>
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
      // display None Function Start
        function langDispNoneFun() {
            var Langhide = document.getElementsByClassName('Language');
            for (var i = 0; i < Langhide.length; i++) {
                Langhide[i].style.display = "None";
            }
        }
        function DBDispNoneFun() {
            var Databasehide = document.getElementsByClassName('Database');
            for (var i = 0; i < Databasehide.length; i++) {
                Databasehide[i].style.display = "None";
            }
        }
        function TestDispNoneFun() {
            var Testinghide = document.getElementsByClassName('Testing');
            for (var i = 0; i < Testinghide.length; i++) {
                Testinghide[i].style.display = "None";
            }
        }
        function FWDispNoneFun() {
            var FrameWorkshide = document.getElementsByClassName('FrameWorks');
            for (var i = 0; i < FrameWorkshide.length; i++) {
                FrameWorkshide[i].style.display = "None";
            }
        }
        function STDispNoneFun() {
            var scriptlhide = document.getElementsByClassName('scriptl');
            for (var i = 0; i < scriptlhide.length; i++) {
                scriptlhide[i].style.display = "None";
            }
        }
        function CDDispNoneFun() {
            var cloudhide = document.getElementsByClassName('cloud');
            for (var i = 0; i < cloudhide.length; i++) {
                cloudhide[i].style.display = "None";
            }
        }
        // display None Function End
        // display block Function Start
        function langDispFun() {
            var Langdisp = document.getElementsByClassName('Language');
            for (var i = 0; i < Langdisp.length; i++) {
                Langdisp[i].style.display = "Block";
            }
        }
        function DBDispFun() {
            var Databasedisp = document.getElementsByClassName('Database');
            for (var i = 0; i < Databasedisp.length; i++) {
                Databasedisp[i].style.display = "Block";
            }
        }
        function TestDispFun() {
            var Testingdisp = document.getElementsByClassName('Testing');
            for (var i = 0; i < Testingdisp.length; i++) {
                Testingdisp[i].style.display = "Block";
            }
        }
        function FWDispFun() {
            var FrameWorksdisp = document.getElementsByClassName('FrameWorks');
            for (var i = 0; i < FrameWorksdisp.length; i++) {
                FrameWorksdisp[i].style.display = "Block";
            }
        }
        function STDispFun() {
            var scriptldisp = document.getElementsByClassName('scriptl');
            for (var i = 0; i < scriptldisp.length; i++) {
                scriptldisp[i].style.display = "Block";
            }
        }
        function CDDispFun() {
            var cloudisp = document.getElementsByClassName('cloud');
            for (var i = 0; i < cloudisp.length; i++) {
                cloudisp[i].style.display = "Block";
            }
        }
        // display Block Function End
        function alldispFun() {
            langDispFun();
            CDDispFun();
            STDispFun();
            FWDispFun();
            TestDispFun();
            DBDispFun();
        }
        function langdispFun() {
            langDispFun();
            CDDispNoneFun();
            STDispNoneFun();
            FWDispNoneFun();
            TestDispNoneFun();
            DBDispNoneFun();
        }
        function cloudispFun() {
            langDispNoneFun();
            CDDispFun();
            STDispNoneFun();
            FWDispNoneFun();
            TestDispNoneFun();
            DBDispNoneFun();
        }
        function framdispFun() {
            langDispNoneFun();
            CDDispNoneFun();
            STDispNoneFun();
            FWDispFun();
            TestDispNoneFun();
            DBDispNoneFun();
        }

        function dbdispFun() {
            langDispNoneFun();
            CDDispNoneFun();
            STDispNoneFun();
            FWDispNoneFun();
            TestDispNoneFun();
            DBDispFun();
        }
        function testdispFun() {
            langDispNoneFun();
            CDDispNoneFun();
            STDispNoneFun();
            FWDispNoneFun();
            TestDispFun();
            DBDispNoneFun();
        }
        function scriptdispFun() {
            langDispNoneFun();
            CDDispNoneFun();
            STDispFun();
            FWDispNoneFun();
            TestDispNoneFun();
            DBDispNoneFun();
        }
        

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
import pymysql
import cgi
import cgitb
cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()
form = cgi.FieldStorage()

stfname = form.getvalue("stname")
stfpass = form.getvalue("stpass")
stloginbtn = form.getvalue("stlogin")

if stloginbtn != None:
    try:
        getid = None
        if stfname == "jaga" and stfpass == '12345':
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
        elif stfname != None and stfpass != None:
            fquery = ("""select id from emp_details where EmpMailId = '%s' and EmpPwd = '%s'""" % (stfname, stfpass))
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
import pymysql
import cgi, random
import cgitb
cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

q = """select max(id) from user_details"""
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

usname = form.getvalue('us-name')
usdob = form.getvalue('us-dob')
usnumber = form.getvalue('us-number')
usaddres = form.getvalue('us-addres')
uspincode = form.getvalue('us-pincode')
usprofession = form.getvalue('us-profession')
usemail = form.getvalue('us-email')
ussubmitbtn = form.getvalue('us-submitbtn')

if ussubmitbtn != None:
    s = slice(3)
    usnameslice = usname[s]
    usprofslice = usprofession[s]
    userid = usnameslice + z + str(n + 1) + usprofslice
    randsymbollist = ['@', '#', '$']
    randsymbol = random.choice(randsymbollist)
    rand1 = random.randint(0, 10)
    rand2 = random.randint(0, 10)
    rand3 = random.randint(0, 10)
    rand4 = random.randint(0, 10)
    uspassword = usnameslice + usprofslice + randsymbol + str(rand1) + str(rand3) + str(rand2) + str(rand4)
    insertuserqu = ("""INSERT INTO user_details (userid, username, useremail, userdob, usernumber, profession,address,pincode,password) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (userid, usname, usemail, usdob, usnumber, usprofession,usaddres, uspincode, uspassword))
    cur.execute(insertuserqu)
    if insertuserqu:
        fromaddr = "karuppasamy.mk.2024@gmail.com"
        mpassword = "ekkilawteoijhjie"
        toaddr = usemail
        subject = "Form Dkast techiezz Learning site"
        body = ("""
        Dear %s
            welcome to Dkast techies site! We are happy to have you join our community of learners and educators
            dedicated to "help to start your career and develop your knowledge in programming".
            
            your account has been successfully created, and you are now ready to embark on your learing journey with us.
            Whether you're here to expand your knowledge, enhance your skills, or connect with like-minded individuals,
            Kkast has everything you need to succeed.
            
            your passowrd is:%s
            don't share with anyone.
            
            We're here to support you every step of the way. If you have any questions, encounter any issues, or simply want to
            feedback, don't hesitate to reach out to our support team at 'karuppasamy.mk.2024@gmail.com'.
        """ % (usname, uspassword))
        msg = """Subject:{}\n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromaddr,mpassword)
        server.sendmail(fromaddr,toaddr,msg)
        server.quit()
        print("""
            <script>
                alert("Password Sented to your mail");
                window.location.href="./index.py";
                $(document).ready(function(){
                        // Open the modal
                        $('#signinbtn').modal('show');
                    });
            </script>
        """)
    else:
        print("""
         <script>
                alert("Error in register... Try agin Later!!!");
                $(document).ready(function(){
                    // Open the modal
                    $('#userregform').modal('show');
                });
        </script>               
    """)

usrname = form.getvalue('u-name')
usrpass = form.getvalue('u-pass')
usrsigninbtn = form.getvalue('usersignin')

if usrsigninbtn != None:
    try:
        getid = ""
        if usrname != None and usrpass != None:
            fquery = ("""select id from user_details where useremail = '%s' and password = '%s'""" % (usrname, usrpass))
            cur.execute(fquery)
            getid = cur.fetchone()
            dbconn.commit()
            dbconn.close()
            if getid != None:
                print("""
                    <script>
                        alert("login Successfully");
                        location.href="./UserDashboard.py?id=%s";
                    </script>
                """ % getid)
            else:
                print("""
                <script>
                    alert("EmailId and Password is incorrect....");
                    $(document).ready(function(){
                        // Open the modal
                        $('#signinbtn').modal('show');
                    });
                </script>               
                """)
    except Exception as e:
        print("""
                <script>
                    alert("EmailId and Password is incorrect....<br> and %s ");
                    $(document).ready(function(){
                        // Open the modal
                        $('#signinbtn').modal('show');
                    });
            </script>               
        """ % e)

dbconn.commit()
dbconn.close()
