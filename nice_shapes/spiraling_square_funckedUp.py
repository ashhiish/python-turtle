# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
from turtle import *   #Outside_In
wn = Screen()
wn.bgcolor("black")
wn.title("Turtle")
skk = Turtle()
skk.speed(0)
skk.color("green")

dkk = Turtle()
dkk.speed(0)
dkk.color("blue")
dkk.up()
dkk.goto(-50,20)
dkk.down()

lkk = Turtle()
lkk.speed(0)
lkk.color("red")
lkk.up()
lkk.goto(-100,30)
lkk.down()

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        dkk.fd(size)
        dkk.left(90)
        lkk.fd(size)
        lkk.left(90)
        size = size-5

for i in range(200):
    sqrfunc(6+i*20)

# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)

# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)

done()