import numpy as np
import cv2
import matplotlib.pyplot as plt

cap=cv2.VideoCapture('vtest.avi')
fgbg=cv2.createBackgroundSubtractorMOG2()
fgbg2=cv2.createBackgroundSubtractorKNN()

while True:
    ret,frame=cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)
    fgmask2 = fgbg2.apply(frame)

    cv2.imshow('Video',frame)
    cv2.imshow('FG Mask MOG2', fgmask)
    cv2.imshow('FG Mask KNN', fgmask2)
    if cv2.waitKey(10)==27:
        break

cap.release()
cv2.destroyAllWindows()