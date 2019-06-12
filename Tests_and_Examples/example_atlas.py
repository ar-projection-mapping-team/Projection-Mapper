import atlastk as Atlas

body = """
<div style="display: table; margin: 50px auto auto auto;">
 <fieldset>
  <input id="x" maxlength="20" placeholder="Enter a name here" type="text"
         data-xdh-onevent="Submit" value="World"/>
  <div style="display: flex; justify-content: space-around; margin: 5px auto auto auto;">
   <button data-xdh-onevent="Submit">Submit</button>
   <button data-xdh-onevent="Clear">Clear</button>
  </div>
 </fieldset>
</div>
"""

def acConnect(this, dom, id):
  dom.setLayout("", body)
  dom.focus("x")

def acSubmit(this, dom, id):
  dom.alert("Hello, " + dom.getContent("x") + "!")
  dom.focus("x")

def acClear(this, dom, id):
  if ( dom.confirm("Are you sure?") ):
    dom.setContent("x", "cleard")
  dom.focus("x")

callbacks = {
  "": acConnect,  # The key is the action label for a new connection.
  "Submit": acSubmit,
  "Clear": acClear,
}

Atlas.launch(callbacks)