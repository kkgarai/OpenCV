import cv2
import numpy as np

img=cv2.imread('lena.jpg')


# Gaussian Pyramid
'''
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)

hr1=cv2.pyrUp(img)
hr2=cv2.pyrUp(lr2)

cv2.imshow("Original Image",img)

cv2.imshow("PyrDown 1 Image",lr1)
cv2.imshow("PyrDown 2 Image",lr2)

cv2.imshow("PyrUp 1 Image",hr1)
cv2.imshow("PyrUp 2 Image",hr2)
'''

cv2.imshow("Original Image",img)

layer=img.copy()
gp=[layer]

for i in range(5):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i+1),layer)


# Laplacian Pyramid
layer=gp[-1]
cv2.imshow("Upper level Laplacian Pyramid",layer)

for i in range(len(gp)-1,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()


