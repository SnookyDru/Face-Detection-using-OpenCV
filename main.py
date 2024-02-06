import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_dectector = cv2.CascadeClassifier('haarcascade_eye.xml')
# reading the input image now
cap = cv2.VideoCapture(0)
# loop to go through every webcam frame
while cap.isOpened():
    # storing the frames in frame
    _, frame = cap.read()

    # converting the BGR frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # using the face detector object to detect faces in the gray image
    # via detectMultiScale() method with the parameters:
    # scaleFactor – 1.1
    # minNeighbors – 4
    faces = face_detector.detectMultiScale(gray, 1.1, 4)

    # for loop to iterate through each detected face in each frame
    for (x, y, w, h) in faces:
    # draw a rectangle on the frame itself using coordinated from faces var
    cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=3)

    # roi = region of interest
    roi_gray = gray[y:y + h, x:x + w]  # grayscale
    roi_color = frame[y:y + h, x:x + w]  # colored

    # hierarchical detection
    eyes = eye_dectector.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        # drawing the bounding box of the eyes
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    # show the frames on the screen with the bounding boxes
    cv2.imshow("window", frame)

    # break the loop if user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame.release()