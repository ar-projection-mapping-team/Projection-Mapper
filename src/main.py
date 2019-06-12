import atlastk as Atlas
import cv2
from src.Shader import Shader
import threading

image_path = '../Test_Images/bird.jpg'
shader = Shader(image_path)

# WEB GUI CODE #
# body: Main page for program's GUI
body = """
<style>
  .slidecontainer {
  width: 100%; /* Width of the outside container */
}

/* The slider itself */
.slider {
  -webkit-appearance: none;  /* Override default CSS styles */
  appearance: none;
  width: 100%; /* Full-width */
  height: 25px; /* Specified height */
  background: #d3d3d3; /* Grey background */
  outline: none; /* Remove outline */
  opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
  -webkit-transition: .2s; /* 0.2 seconds transition on hover */
  transition: opacity .2s;
}

/* Mouse-over effects */
.slider:hover {
  opacity: 1; /* Fully shown on mouse-over */
}

/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.slider::-webkit-slider-thumb {
  -webkit-appearance: none; /* Override default look */
  appearance: none;
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: #4CAF50; /* Green background */
  cursor: pointer; /* Cursor on hover */
}

.slider::-moz-range-thumb {
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: #4CAF50; /* Green background */
  cursor: pointer; /* Cursor on hover */
}
</style>
<div class="slidecontainer">
  <h1>Threshold</h1>
  <input id="threshold_slider" type="range" min="1" max="1000" value="100" class="slider" id="myRange">
  <button data-xdh-onevent="ChangeShader" type="button">Change Shader</button> 
</div>
"""


# WEB GUI FUNCTIONS #
# acConnect: Initializes GUI's main page
def acConnect(this, dom, id):
  dom.setLayout("", body)

# acChangeShader: Will update currently running shader to use selected parameters
def acChangeShader(this, dom, id):
    new_threshold = dom.getContent("threshold_slider")
    update_shader(new_threshold)


# WEB GUI CALLBACKS #
callbacks = {
  "": acConnect,  # The key is the action label for a new connection.
  "ChangeShader": acChangeShader,
}


# ATLAS INIT #
def run_gui():
    Atlas.launch(callbacks)

# Initialize shader thread
def run_shader(threshold_value):
    global shader

    shader.create_shader(threshold_value)
    shader.show_shader()


shader_thread = threading.Thread(target=run_shader, args=(100,))
gui_thread = threading.Thread(target=run_gui)

shader_thread.start()
gui_thread.start()

def update_shader(new_threshold):
    global shader

    print("changing shader with value " + str(new_threshold))

    # TODO: Works only once and not correctly, figure out how to update the threshold value for the shader
    shader.create_shader(int(new_threshold))


