# Import the required modules
import pyautogui as gui
from time import sleep

DISTANCE = 300
CHANGE = 10
PATH = r"#" # Write your saving directory

def Spiral_draw(distance,change):
    """Function to draw spiral"""


    print("Starting In 3 2 1 😮")
    sleep(3)

    while distance > 0:

        gui.drag(distance,0,duration=0.25) # Right
        distance -= change

        gui.drag(0,distance,duration=0.25) # Down
        gui.drag(-distance,0,duration=0.25) # Left

        distance -= change
        gui.drag(0,-distance,duration=0.25) # Up 

def Define_path(path):
    """Defining path to save the file"""

    try:    

        gui.hotkey('ctrl','s')
        gui.write(f"{path}\spiral.jpg")
        gui.click(1398,793)

    except Exception as e:
        print('Something Went Wrong :', e)
    

if __name__ == "__main__":

    Spiral_draw(DISTANCE,CHANGE)
    Define_path(PATH)
    print("Code Completed 🔥")