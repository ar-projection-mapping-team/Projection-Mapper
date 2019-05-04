from flask import Flask, render_template, request
from CalibrationDriver import driver

controller = Flask(__name__)


# TODO: Create home page for GUI and some way to get to calibration screen
@controller.route('/')
def hello_world():
    return "Projection Mapper Web Control"


# Shows controls for projector
@controller.route('/control')
def calibrate_projection():
    # Create a new instance of the calibrator, then start it
    instance = driver
    instance.start()

    # Get user values for calibration threshold and contrast values
    thresh_slider = request.form["thresh_slider"]
    contrast_slider = request.form["contrast_slider"]

    return render_template('ControlGui.html')
