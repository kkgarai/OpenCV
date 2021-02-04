import cv2

# img=cv2.imread('test.jpg')
# img=cv2.resize(img,(920,720))
# print(img.shape)
face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\KIRAN\\AppData\\Local\\Programs\\Python\\Python38\\lib\\"
    "site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(
    "C:\\Users\\KIRAN\\AppData\\Local\\Programs\\Python\\Python38\\lib\\"
    "site-packages\\cv2\\data\\haarcascade_eye_tree_eyeglasses.xml")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    try:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes=eye_cascade.detectMultiScale(roi_gray)
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow("Image", img)
    except:
        break

cap.release()
cv2.destroyAllWindows()
