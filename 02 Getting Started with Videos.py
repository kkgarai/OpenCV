import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Video_captured_from_webcam.avi",fourcc,20.0,(640,480))
# Capture the frames continiously
while True:
    ret,frame=cap.read()

    if ret:
        out.write(frame)

        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT),end=" x ")
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        # It shows the grayscale image
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",gray)

        # Wait for user input and close the window if the user inputs "q" key
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

'''
# to read video from a video file

cap=cv2.VideoCapture("file_path")
'''