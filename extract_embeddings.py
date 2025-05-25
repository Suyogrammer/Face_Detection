import face_recognition
import cv2
import os
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nepal123!",
    database="face_db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pictures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    embedding TEXT
)
""")

for filename in os.listdir("stored_faces"):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    img_path = os.path.join("stored_faces", filename)
    image = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(image)

    if encodings:
        embedding_str = ','.join(map(str, encodings[0].tolist()))
        cursor.execute("INSERT INTO pictures (filename, embedding) VALUES (%s, %s)", (filename, embedding_str))
        print(f"✅ Stored: {filename}")
    else:
        print(f"❌ No face found in {filename}")

conn.commit()
cursor.close()
conn.close()
