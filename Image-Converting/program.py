
import cv2

img = cv2.imread("img/nirob.jpg");
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(9,9),0)

cv2.imshow('Orginal Image',img);
cv2.imshow('Gray IMG',imgGray)
cv2.imshow('Img Blur',imgBlur)

cv2.waitKey(0);