import numpy as np
import cv2
import imutils
import time

# initialize the HOG descriptor/person detector
class Localiser():
    def __init__(self):
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def localise(self, frame):
        #resizing for faster detection
        frame = cv2.resize(frame, (640,480))
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
        # detect person in the image & returns the bounding boxes for the detected person
        boxes, weights = self.hog.detectMultiScale(gray, winStride= (8,8),  padding=(0, 0), scale=1.1)
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)

        return frame
    
    def __del__(self):
        self.cap.release()
        