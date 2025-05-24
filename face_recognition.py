import cv2
import os

img = cv2.imread('Team.jpg')

if img is None:
    print("Error loading image")
else:
    cv2.namedWindow('Real Madrid', cv2.WINDOW_AUTOSIZE)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray RM', gray)

    haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #Detect faces
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=11)

    print(f'Number of faces found = {len(faces)}')

    for i, (x,y,w,h) in enumerate(faces):
        # cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        face = img[y:y+h, x:x+w]
        face_path = os.path.join("stored_faces", f"face_{i+1}.jpg")
        cv2.imwrite(face_path, face)
        print(f"Saved: {face_path}")

    cv2.imshow('Detected Faces', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


