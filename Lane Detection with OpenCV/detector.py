import cv2
import numpy as np
import matplotlib.pyplot as plt


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count=img.shape[2]
    # match_mask_color=(255,)*channel_count
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


# img = cv2.imread('road2.jpg')
# image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def process(image):
    # print(image.shape)
    height, width, _ = image.shape

    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 200)

    cropped_image = region_of_interest(canny_image,
                                       np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi / 60, threshold=150, minLineLength=20, maxLineGap=100)

    def draw_the_lines(image, lines):
        img = np.copy(image)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        return img

    lined_image = draw_the_lines(image, lines)
    return lined_image


# plt.imshow(lined_image)


cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    try:

        ret, frame = cap.read()
        frame = process(frame)
        cv2.imshow('Road', frame)

        if cv2.waitKey(1) == 27:
            break
    except:
        break

cap.release()
cv2.destroyAllWindows()
