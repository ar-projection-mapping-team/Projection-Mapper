from flask import Flask, render_template, request
from Calibration import OutlineCalibration
from multiprocessing import Process, Value
import cv2
import numpy as np

controller = Flask(__name__)
calibrator_process = 0
calibrator = 0
thresh = 50
changed = False

# Process function for image calibrator
def calibrator_driver():
    global calibrator

    input_image = cv2.resize(cv2.imread('Test_Images/car.jpg', 0), (1000, 700))
    calibrator = OutlineCalibration(input_image, 1000, 700)
    # calibrator.show_outlines()
    while(True):
        if changed:
            calibrator.create_edge_image(thresh)
            print("CHANGED IN APP")
        calibrator.show_outlines2()
        print(changed)
        print()


# Home page
@controller.route('/')
def index():
    global calibrator_process

    calibrator_process = Process(target=calibrator_driver, args=())
    #calibrator_process.start()


    return "Projection Mapper Web Control"


# Shows controls for projector
@controller.route('/control', methods=['POST', 'GET'])
def calibrate_projection():
    global thresh, changed, calibrator_process

    # Get user values for calibration threshold and contrast values
    imgthreshold = request.form.get('imgthreshold', 50)
    imgcontrast = request.form.get('imgcontrast', 50)
    if thresh != imgthreshold:
        changed = True
        thresh = imgthreshold
        print("CHANGED IN SERVER")
        print(thresh)
        calibrator_process.start()

    # Update values in calibrator
    #calibrator.create_edge_image(imgthreshold)

    return render_template('ControlGui.html')
