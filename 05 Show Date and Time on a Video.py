import cv2
import datetime

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),end=" x ")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)
'''
#or 
cap.set(3,720)
cap.set(4,1200)
'''

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),end=" x ")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        text='Width:'+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+\
             ' Height:'+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))+\
             " Date:"+str(datetime.datetime.now())

        frame=cv2.putText(frame,text,(10,50),cv2.FONT_ITALIC,1,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()