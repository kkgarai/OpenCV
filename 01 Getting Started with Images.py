import cv2

# Read a image
img=cv2.imread("lena.jpg",-1)

# Show image
cv2.imshow("Image",img)
k=cv2.waitKey(5000)

# Capture our keyboard input
if k==27:     # Pressing Escape key
    cv2.destroyAllWindows()

# Write an image to a file
elif k==ord('s'):
    cv2.imwrite("lena_copy.png",img)
    cv2.destroyAllWindows()
