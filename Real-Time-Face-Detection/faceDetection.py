
import cv2

faceModel = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
myVideo = cv2.VideoCapture(0)

while True:
    nirob, video = myVideo.read()
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    face = faceModel.detectMultiScale(video, 1.1, 4)

    for(x, y, w, h) in face:
        cv2.rectangle(video, (x,y),(x+w, y+h), (255,0,0), 2 )
        cv2.imshow("Niorb", video)
        k = cv2.waitKey(38) & 0xFF == ord('q')
        if k == 27:
            break






