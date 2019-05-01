import cv2
import numpy as np
from Calibration import OutlineCalibration

input_image = cv2.resize(cv2.imread('Test_Images/car.jpg', 0), (1000, 700))

calibrator = OutlineCalibration(input_image, 1000, 700)
calibrator.show_outlines()
