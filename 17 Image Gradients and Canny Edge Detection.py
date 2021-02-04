import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('sudoku.png',0)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.abs(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelX=np.uint8(np.abs(sobelX))

sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelY=np.uint8(np.abs(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)

canny=cv2.Canny(img,100,200)

titles=["Image","Laplacian Gradient","SobelX","SobelY","SobelCombined","Canny"]
images=[img,lap,sobelX,sobelY,sobelCombined,canny]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
