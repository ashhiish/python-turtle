import turtle

# benzeneFlowerTurtle

wn = turtle.Screen()
wn.bgcolor('black')
ttl = turtle.Turtle()
ttl.speed(0)

minusAxis = -100
plusAxis = 100

def buildPot(color:str):
    ttl.speed(2)
    ttl.color(color)
    ttl.penup()
    ttl.goto(-100,0)
    ttl.pendown()
    ttl.begin_fill()
    ttl.right(80)
    ttl.forward(220)
    ttl.left(80)
    ttl.forward(120)
    ttl.left(80)
    ttl.forward(220)
    ttl.end_fill()
    ttl.speed(0)

def buildFlower():
    for i in range(5):
        for j in range(6):
            ttl.forward(50)
            ttl.right(60)
        ttl.right(72)


def flower(color:str,xAxis :int,yAxis:int):
    ttl.penup()
    ttl.goto(xAxis,yAxis)
    ttl.pendown()
    ttl.color(color)
    ttl.begin_fill()
    buildFlower()
    ttl.end_fill()

buildPot(color="Brown")
flower(color="pink",xAxis=0,yAxis=0)
flower(color="white",xAxis=minusAxis,yAxis=minusAxis)
flower(color="violet",xAxis=minusAxis,yAxis=plusAxis)
flower(color="cyan",xAxis=plusAxis,yAxis=plusAxis)
flower(color="blue",xAxis=plusAxis,yAxis=minusAxis)
flower(color="green",xAxis=minusAxis,yAxis=0)
flower(color="red",xAxis=0,yAxis=plusAxis)
flower(color="yellow",xAxis=plusAxis,yAxis=0)


turtle.done()
