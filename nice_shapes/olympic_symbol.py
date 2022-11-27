import turtle
 
# object tr for turtle
tr = turtle.Turtle()
 
# set thickness for each ring
tr.pensize(5)

points = [[-110,-25],[0,-25],[110,-25],[-55,-75],[55,-75]]
colors = ["blue" , "black" , "red" , "yellow" , "green"]

def drawCircle(color:str,xAxis:int,yAxis:int):
    tr.color(color)
    tr.penup()
    tr.goto(xAxis, yAxis)
    tr.pendown()
    tr.circle(45)

for i in range (5):
    drawCircle(colors[i] , xAxis= points[i][0] , yAxis = points [i][1] )


# tr.color("blue")
# tr.penup()
# tr.goto(-110, -25)
# tr.pendown()
# tr.circle(45)
 
# tr.color("black")
# tr.penup()
# tr.goto(0, -25)
# tr.pendown()
# tr.circle(45)
 
# tr.color("red")
# tr.penup()
# tr.goto(110, -25)
# tr.pendown()
# tr.circle(45)
 
# tr.color("yellow")
# tr.penup()
# tr.goto(-55, -75)
# tr.pendown()
# tr.circle(45)
 
# tr.color("green")
# tr.penup()
# tr.goto(55, -75)
# tr.pendown()
# tr.circle(45)