import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('messi5.jpg',0)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

canny=cv2.Canny(img,100,200)

titles=["Image","Canny"]
images=[img,canny]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
