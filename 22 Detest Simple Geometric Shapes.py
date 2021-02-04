import cv2
import numpy as np

img=cv2.imread('shapes.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(imgray,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,approx,0,(0,0,0),5)
    x,y=approx.ravel()[:2]
    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectRatio=w/h
        print(aspectRatio)
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img,"Quadrilateral",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==7:
        cv2.putText(img,"Heptagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

cv2.imshow("Shapes",img)
cv2.imshow("Image Gray",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()