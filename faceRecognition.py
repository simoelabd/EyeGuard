import datetime

import cv2
import face_recognition
import numpy as np
import json
from face_recognition import face_distance
import mysql.connector
from db_conn import ConnectDatabase

def load_database_encodings():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_eyegard'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        if not rows:
            print("No data found in the database.")
            return [], []

        # Extract encodings and names from fetched data
        database_encodings = [np.array(json.loads(row[7])) for row in rows]
        database_names = [row[1] for row in rows]
        return database_encodings, database_names

    except Exception as e:
        print("Error loading database encodings:", e)
        return [], []
def insert_detected_face(name):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_eyegard'
        )
        cursor = conn.cursor()
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Insert the detected face into the database
        cursor.execute("UPDATE students SET date = %s WHERE firstName = %s", (current_datetime,name))
        conn.commit()

        conn.close()
    except Exception as e:
        print("Error inserting detected face into database:", e)

def detecter_visages(image, cascade, database_encodings, database_names):
    try:
        frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(frame_rgb)
        face_encodings = face_recognition.face_encodings(frame_rgb, face_locations)

        for i, face_encoding in enumerate(face_encodings):

            name = "inconnu"

            if len(database_encodings) > 0:
                face_distances = face_distance(database_encodings, face_encoding)
                matches = [distance <= 0.6 for distance in face_distances]
                if True in matches:
                    match_index = matches.index(True)
                    name = database_names[match_index]

                    # Insert detected face into the database
                    insert_detected_face(name)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            visages = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in visages:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(image, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        return image
    except Exception as e:
        print("Error detecting faces:", e)
        return image
    except Exception as e:
        print("Error detecting faces:", e)
        return image


def reconnaissance_facial():
    try:
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        cascade = cv2.CascadeClassifier(cascade_path)
        if cascade.empty():
            print("Error loading cascade classifier.")
            return

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to open the webcam.")
            return


        database_encodings, database_names = load_database_encodings()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read the webcam image.")
                break

            frame = detecter_visages(frame, cascade, database_encodings, database_names)
            cv2.imshow('Facial Recognition', frame)

            key = cv2.waitKey(30)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error in facial recognition loop:", e)

if __name__ == "__main__":
    reconnaissance_facial()
