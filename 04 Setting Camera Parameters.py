import cv2


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

        cv2.imshow("frame", frame)

        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()