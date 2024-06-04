#!C:/Users/Jagathish/AppData/Local/Programs/Python/Python312/python.exe
import cgi, cgitb, pymysql
print("content-type:text/html \r\n\r\n")

form = cgi.FieldStorage()
uid = form.getvalue('id')
ctitle = form.getvalue('title')
cstatus = form.getvalue('status')

cgitb.enable()
dbconn = pymysql.connect(host="localhost", user="root", password="", database="dkast_py_site")
cur = dbconn.cursor()

query = ("""select * from emp_inventory where VidTitle = '%s' && VidChapter = '%s'""" % ( ctitle, cstatus))
cur.execute(query)
data = cur.fetchall()

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
            <div class="uscontent d-flex align-content-center p-3">""")
for i in data:
    vidsrc = "./Resources/videos/" + i[6]
    vidtitle = i[3]
    vidchapter = i[4]
    vidname = i[2]
    viddesc = i[7]
    vidnotes = "./Resources/Notes/" + i[8]
    vidtask = i[9]
    print("""            
                    <div class="container vid-conetent">
                    <div class="p-3 vid-container w-100 h-100">
                        <video id="Videocnt" src="%s" class="vid" controls>
                        </video>
                    </div>
                </div>
                <div class="p-3 usnotes">
                    <div class="usnotesin p-2" id="stick">
                        <!-- <i class="fa-solid fa-circle-check" style="color: #11ee36;"></i> -->
                        <h5>%s</h5>
                        <span class="chap">
                            <h6>%s: </h6>
                            <h6>%s</h6>
                        </span>
                    </div>
                    <div class="usnotesin p-2 mt-2">
                        <h6>Description: </h6>
                        <p>%s</p>
                        <div class="d-flex justify-content-center">
                            <a id="clickdn" type="button" class="btn add-btn" href="%s" download><i
                                    class="fa fa-download pe-2"></i>Download Notes</a>
                        </div>
                    </div>
                    <div class="usnotesin p-2 mt-2">
                        <h6>Task: </h6>
                        <p>%s</p>
                    </div>
                    <div class="out d-flex justify-content-end p-4 gap-3">
                    <form enctype="multipart/form-data" method="post" name="videosubform">
                        <input type="button" class="btn btn-light disabled" value="Prev" name="Prev">
                        <input type="button" class="btn btn-light disabled" value="Next" name="Next">
                        <input type="submit" class="btn btn-success" value="Completed" name="Completed" id="compbutton">
                    </form>
                    </div>
                </div>
            </div>
        </div>
    </div>""" % (vidsrc, vidtitle, vidchapter, vidname, viddesc, vidnotes, vidtask))

print("""
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
            cmpbutton.classList.remove = "disabled";
        });
        video.addEventListener('timeupdate', () => {
            // Check if the video is near the end
            if (video.currentTime >= video.duration - 3) { // You can adjust the threshold as needed
                // Disable the button if the video is dragged to the end
                 cmpbutton.classList.add = "disabled";
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

queryone = ("""select * from emp_inventory where VidTitle = '%s'""" % ctitle)
cur.execute(queryone)
chapcollection = cur.fetchall()
oldchapter = []

for i in chapcollection:
    oldchapter.append(i[4])

# print(oldchapter)
# print(cstatus)
nextchaptercount = 0

for i in range(len(oldchapter)):
    if cstatus == oldchapter[i]:
        nextchaptercount = i + 1
        break
if nextchaptercount == len(oldchapter):
    nextchapter = "Completed"
else:
    nextchapter = oldchapter[nextchaptercount]

# print(nextchapter)

query = """select userid from user_details where id = '%s' """ % uid
cur.execute(query)
getuid = cur.fetchone()

completedbtn = form.getvalue("Completed")

if completedbtn != None:
    upqone = ("""UPDATE course_enroll SET status = '%s' WHERE empid = '%s' && CourseName = '%s'""" % (nextchapter, getuid[0], ctitle))
    cur.execute(upqone)
    dbconn.commit()
    dbconn.close()
    if nextchapter == "Completed":
        print("""
                    <script>
                        alert("Course is completed");
                        window.location.href="./UserCourseList.py?id=%s";
                    </script>
                    """ % uid)
    else:
        print("""
            <script>
                alert("this chapter is completed");
                window.location.href="./UserOnGoingCourse.py?id=%s&title=%s&status=%s";
            </script>
            """ % (uid, ctitle, nextchapter))

dbconn.commit()
dbconn.close()
