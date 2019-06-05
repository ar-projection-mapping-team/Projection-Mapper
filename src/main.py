import atlastk as Atlas
import cv2

# APP INIT #
input_image = cv2.imread('car.jpg', 0)

# WEB GUI CODE #
# body: Main page for program's GUI
body = """
<div style="display: table; margin: 50px 400px auto;">
 <fieldset>
  <h1>Open CV Test</h1>
  <div style="display: flex; justify-content: space-around; margin: 5px auto auto auto;">
   <button data-xdh-onevent="Show">Show</button>
   <button data-xdh-onevent="Unshow">Unshow</button>
  </div>
 </fieldset>
</div>
<div style="margin: 20px 400px auto;">
  <canvas id="image" height="400" width="400" style="border: 2px solid black; display: none"></canvas>
  <script>
  var canvas = document.getElementById("image");
  var ctx = canvas.getContext("2d");
  </script>
</div>
"""

# WEB GUI FUNCTIONS #
# acConnect: Initializes GUI's main page
def acConnect(this, dom, id):
  dom.setLayout("", body)

# acShow: Shows image on 'Show' button press
def acShow(this, dom, id):
    dom.setAttribute("image", "style", "border: 2px solid black; display: show")

# acUnshow: Hides image on 'Unshow' button press
def acUnshow(this, dom, id):
    dom.setAttribute("image", "style", "border: 2px solid black; display: none")

# WEB GUI CALLBACKS #
callbacks = {
  "": acConnect,  # The key is the action label for a new connection.
  "Show": acShow,
  "Unshow": acUnshow,
}

# ATLAS INIT #
Atlas.launch(callbacks)