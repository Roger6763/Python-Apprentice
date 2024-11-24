# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
# Your code here
import turtle
from pathlib import Path
from PIL import Image

screen = turtle.Screen()
screen.setup(width=600, height=600)
tina = turtle.Turtle() 

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    tina.goto(x, y)

def set_turtle_image(turtle, image_name):
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

                 # Create a turtle named tina
set_turtle_image(tina, "moustache1.gif")
set_background_image(screen, "emoji.png") 

screen.onclick(screen_clicked)
turtle.done()   

