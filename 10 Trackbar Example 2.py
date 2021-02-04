"""
Trackbars are used to change out image values dynamically
"""

import numpy as np
import cv2


def nothing(x):
    print(x)



cv2.namedWindow("Image")

cv2.createTrackbar('CP', 'Image', 10, 400, nothing)


switch='color/gray'
cv2.createTrackbar(switch,'Image',0,1,nothing)

while True:
    img = cv2.imread('lena.jpg')
    #img=cv2.imshow("Image", img)

    pos = cv2.getTrackbarPos("CP", "Image")
    cv2.putText(img,str(pos),(50,150),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0))


    if cv2.waitKey(1) == 27:  # for escape key
        break


    s = cv2.getTrackbarPos(switch, "Image")

    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    cv2.imshow("Image", img)

cv2.destroyAllWindows()
