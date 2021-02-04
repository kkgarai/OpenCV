import  cv2
import numpy as np

#img=cv2.imread('lena.jpg',-1)

img=np.zeros((512,512,3),dtype=np.uint8)
img=cv2.line(img,(0,0),(255,255),(0,0,255),2)    # Colour will be in BGR format

img=cv2.arrowedLine(img,(0,255),(255,255),(0,255,255),2)

img=cv2.rectangle(img,(384,0),(255,100),(0,100,105),-1)

img=cv2.circle(img,(390,63),69,(120,0,110),2)

img=cv2.putText(img,"OpenCV",(10,500),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(10,10,10),5,cv2.LINE_AA)


cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()