from turtle import *
import colorsys

bgcolor("black")
tracer(100)
width(7)
h=0
n=50

for i in range(2000):
    c= colorsys.hsv_to_rgb(h,1,.9)
    h += 1/n
    setposition(0,100)
    pencolor(c)
    left(50)
    circle(10)
    backward(42)
    rt(56)
    fd(i)
    bk(575)
done()  

