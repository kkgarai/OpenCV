import cv2
import matplotlib.pyplot as plt

img=cv2.imread('lena.jpg',-1)
'''
cv2.imshow("Image",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
'''

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=["Original Image","BINARY","BINARY_INV","THRESH_TRUNC","TOZERO",'TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()