import cv2


webcam = cv2.VideoCapture(0)

while True:
    _,img = webcam.read()
    cv2.imshow('Hand Gesture Volume Control', img)
    cv2.waitKey(10)