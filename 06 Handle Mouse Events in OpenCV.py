import cv2
import numpy as np

events=[i for i in dir(cv2) if "EVENT" in i]
print(events)

# create a mouse click callback function
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        text=str(x)+" , "+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_ITALIC,0.5,(255,255,0),1)
        cv2.imshow("Image",img)

    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        text=str(blue)+" , "+str(green)+" , "+str(red)
        cv2.putText(img, text, (x, y), cv2.FONT_ITALIC, 0.5, (0, 255, 255), 1)
        cv2.imshow("Image", img)



#img=np.zeros((512,512,3),dtype=np.uint8)
img=cv2.imread('lena.jpg')
cv2.imshow("Image",img)

cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()