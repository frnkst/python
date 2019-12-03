import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier('lib/haarcascade_frontalface_default.xml')

# Capture video from the web cam
capture = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = capture.read()

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 50, 150), 8)

    # Display the image
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
