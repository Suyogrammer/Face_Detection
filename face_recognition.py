import cv2

img = cv2.imread('RM.jpg')

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
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=3)

    print(f'Number of faces found = {len(faces)}')

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv2.imshow('Detected Faces', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()