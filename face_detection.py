# Importing opencv library
import cv2
size = 4

# The internal webcam is called a 0, so we will use that.
webcam = cv2.VideoCapture(0)

# Load the face classifier file.
classifier = cv2.CascadeClassifier('face.xml')

while True:
    (rval, im) = webcam.read()
    # Flip to act as a mirror.
    im=cv2.flip(im,1,1)

    # This is for resizing the image to speed up detection.
    mini = cv2.resize(im, (im.shape[1] // size, im.shape[0] // size))

    # This line code is for detecting faces.
    faces = classifier.detectMultiScale(mini)

    # This draws rectangles around each faces.
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)

    # This shows the output.
    cv2.imshow('Face Detection for SMART ENTRY',   im)
    key = cv2.waitKey(10)


