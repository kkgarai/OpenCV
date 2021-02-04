"""
Trackbars are used to change out image values dynamically
"""

import numpy as np
import cv2


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('R', 'Image', 0, 255, nothing)

switch='0 : OFF\n1 : ON'
cv2.createTrackbar(switch,'Image',0,1,nothing)

while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:  # for escape key
        break

    b = cv2.getTrackbarPos("B", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    r = cv2.getTrackbarPos("R", "Image")
    s = cv2.getTrackbarPos(switch, "Image")

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv2.destroyAllWindows()
