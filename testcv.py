import cv2 as cv

vcap = cv.VideoCapture(0)
while 1:

    ret, frame = vcap.read()
    cv.imshow("VIDEO", frame)
    cv.waitKey(1)
