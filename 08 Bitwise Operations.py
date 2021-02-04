import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), dtype=np.uint8)
img2 = cv2.imread('image_1.jpg')
img2 = cv2.resize(img2, (500, 250))

img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

print(img2.shape)

# Perform Bitwise operations
bitAnd=cv2.bitwise_and(img2,img1)
bitOr=cv2.bitwise_or(img2,img1)
bitXor=cv2.bitwise_xor(img2,img1)
bitNot1=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)

cv2.imshow("Image-1", img1)
cv2.imshow("Image-2", img2)
cv2.imshow('BitAnd',bitAnd)
cv2.imshow("BitOr",bitOr)
cv2.imshow("BitXor",bitXor)
cv2.imshow("BitNot1",bitNot1)
cv2.imshow("BitNot2",bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
