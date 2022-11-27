from turtle import *
import colorsys

setup(800,800)

bgcolor("black")

ttl = Turtle()
ttl.speed(0)
#tracer(10)
ttl.width(2)

for j in range(25):
    for i in range(15):
        ttl.color(colorsys.hsv_to_rgb(i/15, j/25, 1))
        ttl.right(90)
        ttl.circle(200-j*4,90)
        ttl.left(90)
        ttl.circle(200-j*4,90)
        ttl.right(180)
        ttl.circle(50,24)

done()