"""""

Write a program tha""Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

def set_turtle_image(turtle, image_name):
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    screen.setup(image.width, image.height, startx=0, starty=0)
    screen.bgpic(image_path)

tina = turtle.Turtle()                  # Create a turtle named tina
set_turtle_image(tina, "moustache1.gif")


set_background_image(screen, "emoji.png") 

turtle.done()   