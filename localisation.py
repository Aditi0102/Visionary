import numpy as np
import cv2
import imutils
import time

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

cap = cv2.VideoCapture("./Data/Dummy/1.mp4")

frameCount = 0
start_time = time.time()
 
while(True):

    ret, frame = cap.read() 
    cv2.waitkey(30)
    
    #resizing for faster detection
    frame = cv2.resize(frame, (640,480))
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
   
    # detect person in the image & returns the bounding boxes for the detected person
    boxes, weights = hog.detectMultiScale(gray, winStride= (8,8),  padding=(0, 0), scale=1.1)

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(30)
