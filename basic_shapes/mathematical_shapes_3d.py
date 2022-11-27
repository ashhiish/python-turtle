import turtle 
  
# Forming the window screen
tut = turtle.Screen()
tut.title("Mathematical Shapes 3d")
ttl = turtle.Turtle()

# cube
# object color
ttl.color("orange")
ttl.begin_fill()    
# forming front square face
for i in range(4):
    ttl.forward(100)
    ttl.left(90)
# bottom left side
ttl.goto(50,50)
# forming back square face
for i in range(4):
    ttl.forward(100)
    ttl.left(90)
# bottom right side
ttl.goto(150,50)
ttl.goto(100,0)
# top right side
ttl.goto(100,100)
ttl.goto(150,150)
# top left side
ttl.goto(50,150)
ttl.goto(0,100)
ttl.end_fill()  

ttl.reset()

# cuboid

ttl.color("green")
ttl.begin_fill()
# forming front rectangle face
for i in range(2):
    ttl.forward(100)
    ttl.left(90)
    ttl.forward(150)
    ttl.left(90)
  
# bottom left side
ttl.goto(50,50)
  
# forming back rectangle face
for i in range(2):
    ttl.forward(100)
    ttl.left(90)
    ttl.forward(150)
    ttl.left(90)
  
# bottom right side
ttl.goto(150,50)
ttl.goto(100,0)
  
# top right side
ttl.goto(100,150)
ttl.goto(150,200)
  
# top left side
ttl.goto(50,200)
ttl.goto(0,150)

ttl.end_fill()

ttl.reset()

# cylinder 

from turtle import *

color(0.2, 0.5, 0.8)

ttl.forward(100)
ttl.color("black")
ttl.begin_fill()
ttl.circle(20)
ttl.end_fill()

#ttl.setheading(90)
ttl.penup()
ttl.left(90)
ttl.forward(2*20)
ttl.left(90)
ttl.pendown()
#ttl.setheading(180)
ttl.forward(100)

ttl.circle(20, extent=180)  #  Draw 1/2 of the bottom/circle

turtle.done()