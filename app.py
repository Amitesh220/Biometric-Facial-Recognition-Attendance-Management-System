import face_recognition
import cv2
import numpy as np
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector as conn

app = Flask(__name__)
CORS(app)

db = []
known_path = os.path.join(os.getcwd(), "Images/Known_faces/")
unknown_path = os.path.join(os.getcwd(), "Images/Unknown_faces/")

def get_data():
    global db
    db.clear()  
    con = conn.connect(host='yourhost', database='yourdb', user='yourusername', password='yourpassword', charset='utf8', port=yourportnumber)
    cursor = con.cursor()
    sql = 'SELECT * FROM register'
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        l = []
        l.append(i[0])
        string = i[1][1:-2]
        nums = []
        for x in string.split():
            nums.append(float(x.strip()))
        l.append(nums)
        db.append(l)
    cursor.close()
    con.close()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET'])
def register():
    con = conn.connect(host='yourhost', database='yourdb', user='yourusername', password='yourpassword', charset='utf8', port=yourportnumber)
    cursor = con.cursor()
    sql = 'INSERT INTO register (name, encoding) VALUES (%s, %s)'
    name = request.args.get("name")
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    if face_encodings:
        dir = os.path.join(known_path, name)
        if not os.path.isdir(dir):
            os.mkdir(dir)
        os.chdir(dir)
        rand_no = np.random.random_sample()
        cv2.imwrite(str(rand_no) + ".jpg", frame)
        encoding = ",".join(map(str, face_encodings[0]))
        cursor.execute(sql, (name, encoding))
        con.commit()
    video_capture.release()
    cv2.destroyAllWindows()
    cursor.close()
    con.close()
    return "Done"

@app.route('/mark_attendance', methods=['GET'])
def mark_attendance():
    get_data()
    global db
    msg = "No face detected. Please try again."
    if db:
        known_face_encodings = [np.array(i[1]) for i in db]
        known_face_names = [i[0] for i in db]
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        if face_encodings:
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                if name != "Unknown":
                    msg = f"Attendance marked for {name}."
                    con = conn.connect(host='yourhost', database='yourdb', user='yourusername', password='yourpassword', charset='utf8', port=yourportnumber)
                    cursor = con.cursor()
                    cursor.execute('INSERT INTO attendance (name) VALUES (%s)', (name,))
                    con.commit()
                    cursor.close()
                    con.close()
                face_names.append(name)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            os.chdir(unknown_path)
            rand_no = np.random.random_sample()
            cv2.imwrite(str(rand_no) + ".jpg", frame)
        video_capture.release()
        cv2.destroyAllWindows()
    return msg

@app.route('/attendance', methods=['GET'])
def attendance():
    con = conn.connect(host='yourhost', database='yourdb', user='yourusername', password='yourpassword', charset='utf8', port=yourportnumber)
    cursor = con.cursor()
    cursor.execute('SELECT * FROM attendance')
    attendance_records = cursor.fetchall()
    cursor.close()
    con.close()
    return jsonify(attendance_records)

if __name__ == '__main__':
    app.run(debug=True)
