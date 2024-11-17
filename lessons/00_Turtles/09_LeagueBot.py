""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.turtlesize(stretch_wid=5, stretch_len=5, outline=2)
def set_turtle_image(turtle, image_name):
   
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    print(image_path)
    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
   
set_turtle_image(t, "leaguebot_bolt.gif")
t.pencolor("blue")
t.penup()
t.goto(-240,-240)
t.pendown()
for i in range(4):
    t.forward(500)
    t.left(90)
    

turtle.done()