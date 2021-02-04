'''
Morphological Transformations are the simple operations based on Image Shape.
They are normally performed on binary images.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((4,4), np.uint8)

dilation = cv2.dilate(mask, kernel,iterations=2)
erosion=cv2.erode(mask,kernel,iterations=2)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2)  # Erosion followed by Dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=2)  # Dilation followed by Erosion
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel,iterations=2)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel,iterations=2)
bh=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel,iterations=2)

titles = ["Image", 'Mask', "Dilation","Erosion","Opening","Closing","mg","th","bh"]
images = [img, mask, dilation,erosion,opening,closing,mg,th,bh]

for i in range(len(images)):
    plt.subplot(2, 5, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
