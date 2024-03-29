import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()


    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


videoCapture.release()
cv2.destroyAllWindows()
