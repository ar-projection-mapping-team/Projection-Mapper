import cv2
import numpy as np


image = cv2.resize(cv2.imread('Test_Images/coffee.jpg', 0), (1000, 700))
edge = cv2.Canny(image, 100, 240)
cv2.imshow('output', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
averageValue = int(np.median(image))
high, x = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
low = 0.8 * high
"""
