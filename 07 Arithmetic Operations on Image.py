import numpy as np
import cv2

img=cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape)    # returns tuple of number of rows ,columns and channela
print(img.size)     # returns total number of pixels
print(img.dtype)    # returns image datatype

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

# ROI (Region of Interest)
ball=img[280:340,330:390]
img[273:333,100:160]=ball

# Resize images
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))



# Add two images
dst=cv2.add(img,img2)
cv2.imshow("Merged",dst)


# Add Weighted
dstW=cv2.addWeighted(img,0.9,img2,0.1,0)
cv2.imshow("Weighted Add",dstW)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()