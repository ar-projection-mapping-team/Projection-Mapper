import atlastk as Atlas
from Shader import DefaultShader, DepthShader
import threading


# CONSTANTS #

# Default shader values for threshold, contrast and brightness
DEFAULT_SHADER_THRESHOLD = 500
DEFAULT_SHADER_CONTRAST = 0
DEFAULT_SHADER_BRIGHTNESS = 0
DEFAULT_SHADER_HUE_LOWERBOUND = 0
DEFAULT_SHADER_HUE_UPPERBOUND = 179

# Path to html GUI file
WEB_GUI = "Main.html"

# GUI FUNCTIONS #

# acConnect: Initializes GUI's main page
def acConnect(this, dom, id):
  dom.setLayout("", Atlas.readAsset(WEB_GUI))

# acChangeShader: Will update currently running shader to use selected parameters
def acChangeShader(this, dom, id):
    new_threshold = dom.getContent("threshold_slider")
    new_contrast = dom.getContent("contrast_slider")
    new_brightness = dom.getContent("brightness_slider")
    update_shader(new_threshold, new_contrast, new_brightness)

# acResetShader: Will reset the shader to the default values
def acResetShader(this, dom, id):
    update_shader(DEFAULT_SHADER_THRESHOLD, DEFAULT_SHADER_CONTRAST, DEFAULT_SHADER_BRIGHTNESS)


# WEB GUI CALLBACKS #
callbacks = {
  "": acConnect,  # The key is the action label for a new connection.
  "ChangeShader": acChangeShader,
  "ResetShader": acResetShader
}


# PROGRAM FUNCTIONS #

# Atlas initialization
def run_gui():
    Atlas.launch(callbacks)

# Shows shader window
def show_shader_screen():
    global shader
    shader.show_shader()

# Updates shader
def update_shader(threshold, contrast, brightness):
    global shader

    # Log changes to shader
    print("-- Updating Shader --")
    print("  Changing threshold value to: " + str(threshold))
    print("  Changing contrast value to: " + str(contrast))
    print("  Changing brightness value to: " + str(brightness) + "\n")

    # Update shader (create a new shader with the new parameters using the 'create_shader' function)
    shader.create_shader(int(threshold), int(contrast), int(brightness))


# TEST PROGRAM #

# Initialize shader (give input image and create initial shader with default parameters)
image_path = '../Tests_and_Examples/Test_Images/LeMonke.png'

# Creates a default shader with default values
# shader = DefaultShader(image_path)
# shader.create_shader(
#     DEFAULT_SHADER_THRESHOLD,
#     DEFAULT_SHADER_CONTRAST,
#     DEFAULT_SHADER_BRIGHTNESS
# )

# Creates a depth shader with default values
shader = DepthShader(image_path)
shader.create_shader(
    DEFAULT_SHADER_HUE_UPPERBOUND,
    DEFAULT_SHADER_HUE_LOWERBOUND,
    DEFAULT_SHADER_CONTRAST,
    DEFAULT_SHADER_BRIGHTNESS
)

# Create and run separate threads for program's web GUI and shader function
shader_thread = threading.Thread(target=show_shader_screen)
gui_thread = threading.Thread(target=run_gui)
shader_thread.start()
gui_thread.start()
