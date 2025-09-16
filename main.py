
#The imports
from keyboard-master import keyboard
#Checks for W
def on_keydown(event):
    
    if event.name == "w":
        output_div = document.querySelector("#WArea")
        output_div.innerHTML = "W was pressed"
keyboard.on_press(on_keydown)
#Checks for S
def on_keydown(event):
    if event.name == "s":
        output_div = document.querySelector("#SArea")
        output_div.innerHTML = "S was pressed"
keyboard.on_press(on_keydown)


#keep it running

keyboard.wait()



