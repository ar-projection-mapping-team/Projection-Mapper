import cv2
from Tests_and_Examples.Calibration import OutlineCalibration


class driver:

    # Load in the image, create the calibrator
    def __init__(self):
        self.input_image = cv2.resize(cv2.imread('Test_Images/car.jpg', 0), (1000, 700))
        self.calibrator = OutlineCalibration(self.input_image, 1000, 700)

    # Starts the calibration program
    def start(self):
        self.calibrator.show_outlines()
