import cv2
import numpy as np

width = 0
height = 0


def shader(preshaded_image, x):
    global width, height

    shaded = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
    B = 4 * x
    G = int(200 / x)
    R = 2 * x + 40
    for i in range(height - 1):
        for j in range(width - 1):
            if preshaded_image[i][j] > 200:
                shaded[i][j] = (B, G, R)
                shaded[i + 1][j] = (B, G, R)
                shaded[i - 1][j] = (B, G, R)

    return shaded

image = cv2.resize(cv2.imread('Test_Images/coffee.jpg', 0), (1000, 700))
width = 1000
height = 700
edge = cv2.Canny(image, 100, 240)

x_1 = 1
while(True):
    if x_1 > 30:
        x_1 = 1
    shaded_image = shader(edge, x_1)
    cv2.imshow('Edge Calibration', shaded_image)
    cv2.waitKey(5)
    x_1 = x_1 + 1

cv2.destroyAllWindows()