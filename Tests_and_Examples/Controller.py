from flask import Flask, render_template, request
from Tests_and_Examples.Calibration import OutlineCalibration
from multiprocessing import Process
import cv2

imgthreshold = 50
imgcontrast = 50

controller = Flask(__name__)


def calibrator_driver(t, c):

    print(t)
    print(c)

    input_image = cv2.resize(cv2.imread('Test_Images/car.jpg', 0), (1000, 700))
    calibrator = OutlineCalibration(input_image, 1000, 700, t, c)
    calibrator.show_outlines()


# TODO: Create home page for GUI and some way to get to calibration screen
@controller.route('/')
def hello_world():
    return "Projection Mapper Web Control"


# Shows controls for projector
@controller.route('/control', methods=['POST', 'GET'])
def calibrate_projection():
    global imgthreshold, imgcontrast

    #p = Process(target=calibrator_driver, args=())
    #p.start()

    # Get user values for calibration threshold and contrast values
    imgthreshold = int(request.form.get('imgthreshold', 50))
    imgcontrast = int(request.form.get('imgcontrast', 50))

    p = Process(target=calibrator_driver, args=(imgthreshold, imgcontrast))
    p.start()

    return render_template('ControlGui.html')
