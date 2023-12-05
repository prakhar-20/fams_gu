from flask import Flask, url_for
from flask import render_template
from flask import request, redirect,Response
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
from flask import Flask, request, jsonify, make_response , send_file
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
#import jwt
import datetime as dt
from functools import wraps
import sys
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import io
import csv
import pandas as pd
from werkzeug.utils import secure_filename
import os
import cv2
import pickle
import numpy as np
import pandas as pd
import face_recognition
from random import randint 
from time import sleep
from flask import Flask, session
from flask_session import Session
app = Flask(__name__)
app.secret_key="anystringhere"
app.config['UPLOAD_FOLDER'] = './static/imagedata'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy()
app.app_context().push()
bootstrap = Bootstrap(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///db.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class User(UserMixin, db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column( db.String, unique=True, nullable = False)
    password = db.Column( db.String, nullable = False)
    email = db.Column( db.String, nullable = False)
    name = db.Column(db.String, nullable = False)



class Subject(db.Model):
    __tablename__= 'subject'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    subjectcode = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Semester(db.Model):
    __tablename__= 'semester'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course = db.Column(db.String)
    semester = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Course(db.Model):
    __tablename__= 'course'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course = db.Column(db.String)
    section = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Room(db.Model):
    __tablename__= 'rooms'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    room_no = db.Column(db.String)
    camera_ip = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Timeslot(db.Model):
    __tablename__= 'timeslot'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    timeslot = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Faculty(db.Model):
    __tablename__= 'faculty'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    regno = db.Column(db.String)
    name = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class Dummyattendance(db.Model):
    __tablename__= 'dummyattendance'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    admission_no = db.Column(db.String)
    name = db.Column(db.String)
    status = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Student(db.Model):
    __tablename__= 'student'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable = False)
    admission_no = db.Column(db.String, unique = True)
    enrollment_no = db.Column(db.Integer, unique = True)
    name = db.Column(db.String)
    dob = db.Column(db.String)
    gender = db.Column(db.String)
    mob = db.Column(db.String)
    email = db.Column(db.String)
    course = db.Column(db.String)
    section = db.Column(db.String)
    semester = db.Column(db.Integer)
    image = db.Column(db.String)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class AttendanceSession(db.Model):
    __tablename__= 'attendancesession'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable = False)
    course = db.Column(db.String)
    section = db.Column(db.String)
    room = db.Column(db.String)
    semester = db.Column(db.String)
    subjectcode = db.Column(db.String)
    facultycode = db.Column(db.String)
    timeslot = db.Column(db.String)
    doa = db.Column(db.String)
    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Attendance(db.Model):
    __tablename__= 'attendance'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable = False)
    attendanceid = db.Column(db.Integer)
    name = db.Column(db.String)
    admissionno = db.Column(db.String)
    enrollmentno = db.Column(db.String)
    status = db.Column(db.String)
    studentid = db.Column(db.Integer)
    
    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



SECRET_KEY = os.urandom(32)
app.config['UPLOAD_FOLDER'] = './static/imagedata'
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def updateattendancelive(attendanceid, studentid):
    db.session.query(Attendance).filter(Attendance.attendanceid==attendanceid , Attendance.studentid == studentid ).update({Attendance.status :"P"}, synchronize_session = False)
    db.session.commit()

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=2, max=60)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



camera = cv2.VideoCapture('joe.jpeg')

with open('./models/7.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)
print(type(all_face_encodings))
known_face_names = list(all_face_encodings.keys())
known_face_encodings = np.array(list(all_face_encodings.values()))

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
attendanceid = 0
presentli = []
def hello():
    print('hello')
def gen_frames():

    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

            # Only process every other frame of video to save time
           
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            global presentli
            presentli =[]
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    studentid = known_face_names[best_match_index]
                    print(type(studentid))
                    name = studentid
                    if studentid not in presentli:
                        presentli.append(studentid)
                        hello()
                print(presentli)
                
                face_names.append(name)
            

            # Display the results
            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, "", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# homepage
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route("/details/subject", methods=["GET"])
@login_required
def subjectdetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Subject).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/course", methods=["GET"])
@login_required
def coursedetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Course).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/attendance/<id>", methods=["GET"])
@login_required
def attedancepushpull(id):
    global presentli
    if request.method == "GET":
        li = []
        for studentid in presentli:
            db.session.query(Attendance).filter(Attendance.attendanceid==id , Attendance.studentid == studentid ).update({Attendance.status :"P"}, synchronize_session = False)
            db.session.commit()
        students = db.session.query(Attendance).filter(Attendance.attendanceid == id, Attendance.status == "P").all()
        for i in students:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)


@app.route("/details/coursename", methods=["GET"])
@login_required
def coursenamedetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Course.course).distinct().all()
        for i in subjects:
            li.append({
                "course":i.course
            })
        print(li)
        return jsonify(li)

@app.route("/details/room", methods=["GET"])
@login_required
def roomdetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Room).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/timeslot", methods=["GET"])
@login_required
def timeslotdetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Timeslot).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/faculty", methods=["GET"])
@login_required
def facultydetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Faculty).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/subjectcode", methods=["GET"])
@login_required
def subjectcodedetails():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Subject).all()
        for i in subjects:
            li.append(i.as_dict())
            del li[-1]['name']
        print(li)
        return jsonify(li)

@app.route("/details/student/<admo>", methods=["GET"])
@login_required
def studentdetailsforupdate(admo):
    username = current_user.username
    if request.method == "GET":
        li = []
        students = db.session.query(Student).filter(Student.admission_no == admo).all()
        for i in students:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/updateapi/<room>/<course>/<section>/<semester>/<subject>/<faculty>/<doa>/<timeslot>", methods=["GET"])
@login_required
def updatedetailsapi(room,course,section,semester,subject,faculty,doa,timeslot):
    username = current_user.username
    if request.method == "GET":
        li = []
        data = db.session.query(AttendanceSession)
        if room != "None":
            data = data.filter(AttendanceSession.room == room)
        if course != "None":
            data = data.filter(AttendanceSession.course == course)
        if semester != "None":
            data = data.filter(AttendanceSession.semester == semester)
        if section != "None":
            data = data.filter(AttendanceSession.section == section)
        if subject != "None":
            data = data.filter(AttendanceSession.subjectcode == subject)
        if faculty != "None":
            data = data.filter(AttendanceSession.facultycode == faculty)
        if doa != "None":
            data = data.filter(AttendanceSession.doa == doa)
        if timeslot != "None":
            data = data.filter(AttendanceSession.timeslot == timeslot)
        data = data.all()

        for i in data:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/attendance/update", methods=["GET"])
@login_required
def attendaceupdate():
    if request.method =="GET":
        return render_template("attendanceupdatedetails.html")

@app.route("/attendance/update/<id>", methods=["GET","POST"])
@login_required
def attendanceupdateid(id):
    if request.method =="GET":
        details = db.session.query(AttendanceSession).filter(AttendanceSession.id==id).first()
        data = db.session.query(Attendance).filter(Attendance.attendanceid==id).order_by(Attendance.name).all()

        return render_template("updateattendance.html", data = data, details = details)
    if request.method =="POST":
        data = db.session.query(Attendance).filter(Attendance.attendanceid==id).all()
        for i in data:
            id = i.id
            name = "checkboxname_"+str(id)
            op = request.form.get(name) != None
            if op == True:
                db.session.query(Attendance).filter(Attendance.id==id).update({Attendance.status :"P"}, synchronize_session = False)
            else:
                db.session.query(Attendance).filter(Attendance.id==id).update({Attendance.status :"A"}, synchronize_session = False)
            db.session.commit()

        return redirect("/attendance/update")

@app.route("/attendance/download/<id>", methods=["GET","POST"])
@login_required
def downloadattendnce(id):
    if request.method =="GET":
        details = db.session.query(AttendanceSession).filter(AttendanceSession.id==id).first()
        data = db.session.query(Attendance.enrollmentno,Attendance.admissionno, Attendance.name, Attendance.status).filter(Attendance.attendanceid==id).all()
        df = pd.DataFrame(data)
        print(df)
        df.rename(columns = {'enrollmentno':'Enrollment No', 'admissionno':'Admission No','name':'Name','status':'Status'},inplace = True)
        df = df.sort_values(by=['Name'], ascending=True)

        filename = "attendance.xlsx"
        df.to_excel(filename, sheet_name = "Attendance" , index=False)
        return send_file(filename)
    if request.method =="POST":
        data = db.session.query(Attendance).filter(Attendance.attendanceid==id).all()
        for i in data:
            id = i.id
            name = "checkboxname_"+str(id)
            op = request.form.get(name) != None
            if op == True:
                db.session.query(Attendance).filter(Attendance.id==id).update({Attendance.status :"P"}, synchronize_session = False)
            else:
                db.session.query(Attendance).filter(Attendance.id==id).update({Attendance.status :"A"}, synchronize_session = False)
            db.session.commit()

        return redirect("")


@app.route("/dummyattendance", methods=["GET"])
@login_required
def dummyattendance():
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Dummyattendance).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/course/<coursename>", methods=["GET", "POST"])
@login_required
def coursedetailscoursename(coursename):
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Course).filter(Course.course==coursename).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route("/details/semester/<coursename>", methods=["GET"])
@login_required
def semesterdetailscoursename(coursename):
    username = current_user.username
    if request.method == "GET":
        li = []
        subjects = db.session.query(Semester).filter(Semester.course==coursename).all()
        for i in subjects:
            li.append(i.as_dict())
        print(li)
        return jsonify(li)

@app.route('/')
@login_required
def login1():
    return render_template('index.html')

@app.route('/dummycourse')
@login_required
def dummycourse():
    return render_template('course.html',courseid = 'inputcoursejs')


@app.route("/student", methods=["GET"])
@login_required
def student():
    if request.method =="GET":
        return render_template("student.html")


@app.route("/attendance", methods=["GET"])
@login_required
def attendance():
    if request.method =="GET":
        return render_template("attendance.html")

@app.route("/attendance/add", methods=["GET","POST"])
@login_required
def addattendance():
    if request.method =="GET":
        return render_template("attendancedetails.html")
    if request.method =="POST":
        room = request.form['room']
        course = request.form['course']
        section = request.form['section']
        semester = request.form['semester']
        subjectcode = request.form['subjectcode']
        facultycode = request.form['facultycode']
        doa = request.form['doa']
        timeslot = request.form['timeslot']
        data = AttendanceSession(course = course, section =  section, semester = semester , room = room, subjectcode = subjectcode, facultycode = facultycode, timeslot = timeslot, doa=doa)
        db.session.add(data)
        db.session.commit()
        data = db.session.query(AttendanceSession).filter(AttendanceSession.course == course, AttendanceSession.section ==  section, AttendanceSession.semester == semester , AttendanceSession.room == room, AttendanceSession.subjectcode == subjectcode, AttendanceSession.facultycode == facultycode, AttendanceSession.timeslot == timeslot, AttendanceSession.doa == doa).first()


        subjects = db.session.query(Subject).filter(Subject.subjectcode == subjectcode).first()
        subject = subjects.name
        facultys = db.session.query(Faculty).filter(Faculty.regno == data.facultycode).first()
        faculty = facultys.name
        datid = data.id
        students = db.session.query(Student).filter(Student.course == course, Student.section == section, Student.semester == semester).all()
        for data in students:
            data = Attendance(attendanceid = datid , name = data.name, admissionno = data.admission_no, enrollmentno =  data.enrollment_no , status = "A", studentid = data.id)
            db.session.add(data)
            db.session.commit()
        return redirect("/takeattendance/"+str(datid))

@app.route("/takeattendance/<id>", methods=["GET"])
@login_required
def takeattendance(id):
    data = db.session.query(AttendanceSession).filter(AttendanceSession.id == int(id)).first()
    course = data.course
    room = data.room
    semester = data.semester
    timeslot = data.timeslot
    section = data.section
    doa = data.doa
    subjectcode = data.subjectcode
    subjects = db.session.query(Subject).filter(Subject.subjectcode == subjectcode).first()
    subject = subjects.name
    facultys = db.session.query(Faculty).filter(Faculty.regno == data.facultycode).first()
    faculty = facultys.name
    datid = int(id)
    courseids = db.session.query(Course).filter(Course.course == course, Course.section == section).first()
    courseid = courseids.id
    roomips = db.session.query(Room).filter(Room.room_no == room).first()
    roomip = roomips.camera_ip

    global camera
    global all_face_encodings
    global known_face_names
    global known_face_encodings
    global attendanceid

    attendanceid = datid
    if request.method =="GET":

        camera = cv2.VideoCapture(roomip)
        with open('./models/'+str(courseid)+'.dat', 'rb') as f:
	        all_face_encodings = pickle.load(f)
        print(type(all_face_encodings))
        known_face_names = list(all_face_encodings.keys())
        known_face_encodings = np.array(list(all_face_encodings.values()))

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        attendanceapi = "details/attendance/"+id
    return render_template("addattendance.html", attenid = id, course = course, section = section , semester = semester, room = room, timeslot = timeslot , faculty = faculty , subject = subject ,attendanceapi = attendanceapi , doa = doa)



@app.route("/student/add", methods=["GET","POST"])
@login_required
def addstudent():
    if request.method =="GET":
        return render_template("addstudent.html")
    if request.method =="POST":
        name = request.form['studentname']
        admission_no = request.form['admissionno']
        enrollment_no = request.form['enrollmentno']
        dob = request.form['dob']
        gender = request.form['gender']
        mob = request.form['mobile']
        email = request.form['email']
        course = request.form['course']
        section = request.form['section']
        semester = request.form['semester']
        data = db.session.query(Student).all()
        a = str(data[-1].id)
        a = int(a)+1
        
        newid = str(a)

        print(request.files)
        file = request.files['photo']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            ext = filename.split(".")[-1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(a)+"."+ext))
            data = Student(name= name, admission_no = admission_no, dob = dob, gender = gender,enrollment_no = enrollment_no , mob=mob, email = email, course = course, section =  section, semester = semester , image = str(a)+"."+ext)
            db.session.add(data)
            db.session.commit()
            sections = db.session.query(Course).filter(Course.course==course, Course.section == section).first()
            datid = str(sections.id)
            with open('./models/'+datid+'.dat', 'rb') as f:
                all_face_encodings = pickle.load(f)
                print(type(all_face_encodings))
                known_face_names = list(all_face_encodings.keys())
                known_face_encodings = np.array(list(all_face_encodings.values()))
            new_image = face_recognition.load_image_file("static/imagedata/"+str(a)+"."+ext)
            new_image_encoding = face_recognition.face_encodings(new_image)[0]
            all_face_encodings[newid] = new_image_encoding
            with open('./models/'+datid+'.dat', 'wb') as f:
                pickle.dump(all_face_encodings, f)

            return redirect("/student")
        return None


@app.route("/student/update", methods=["GET","POST"])
@login_required
def updatestudent():
    if request.method =="GET":
        return render_template("updatestudent.html")

@app.route("/developer", methods=["GET"])
@login_required
def developer():
    if request.method =="GET":
        return render_template("developer.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template('login_register.html')
    if request.method =="POST":
        form = request.form
        remember= request.form.getlist('remember')
        if len(remember)>0:
            rem = True
        else:
            rem=False

        print(form['username'])
    
        user = User.query.filter_by(username=form['username']).first()
        if user:
            if check_password_hash(user.password, form['password']):
                login_user(user,remember = rem)

                #return redirect('/dashboard')
                return redirect(url_for('login1'))
            
    return render_template('login_register.html', form=form)
    
    
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method =="GET":
        return render_template('login_register.html')
    if request.method =="POST":
        form = request.form
        
        user = db.session.query(User).filter(User.username==form['username']).first()
        # to check if user exists or not in User table
        
        if user == None:

            hashed_password = generate_password_hash(form['password'], method='pbkdf2')
            new_user = User(username=form['username'], email=form['email'], password=hashed_password , name = form['fullname'])
            db.session.add(new_user)
            db.session.commit()
            #mailsignup.delay(form.email.data,form.username.data)
            return redirect(url_for('login1'))
            return redirect('/done')
        else:
            return 'Sorry the username already exist'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(host = '0.0.0.0',debug = True,port = 8080) 