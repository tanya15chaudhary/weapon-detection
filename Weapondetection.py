import numpy as np
import cv2
import imutils

gun_cascade = cv2.CascadeClassifier('cascade.xml')
if gun_cascade.empty():
    print("Error: Unable to load the cascade classifier.")
    exit()

camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False

while True:
    ret, frame = camera.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    if len(guns) > 0:
        gun_exist = True
    for (x, y, w, h) in guns:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    cv2.imshow("Security feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

if gun_exist:
    print("Guns detected")
else:
    print("Guns not detected")

camera.release()
cv2.destroyAllWindows()