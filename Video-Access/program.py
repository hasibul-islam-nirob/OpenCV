
import cv2

myVideo = cv2.VideoCapture(0)
while True:
    myImg, img = myVideo.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
