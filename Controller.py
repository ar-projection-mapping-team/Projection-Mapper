from flask import Flask, render_template, request
from Calibration import OutlineCalibration
from multiprocessing import Process
import cv2
import numpy as np

controller = Flask(__name__)


def calibrator_driver():
    input_image = cv2.resize(cv2.imread('Test_Images/car.jpg', 0), (1000, 700))
    calibrator = OutlineCalibration(input_image, 1000, 700)
    calibrator.show_outlines()


# TODO: Create home page for GUI and some way to get to calibration screen
@controller.route('/')
def hello_world():
    return "Projection Mapper Web Control"


# Shows controls for projector
@controller.route('/control', methods=['POST', 'GET'])
def calibrate_projection():

    p = Process(target=calibrator_driver, args=())
    p.start()

    # Get user values for calibration threshold and contrast values
    #imgthreshold = request.form["imgthreshold"]
    #imgcontrast= request.form["imgcontrast"]
    imgthreshold = request.form.get('imgthreshold', None)
    imgcontrast = request.form.get('imgcontrast', None)
    print(imgcontrast)
    print(imgthreshold)


    return render_template('ControlGui.html')
