from turtle import *

bgcolor("black")


ttl = Turtle()
ttl.speed(100)
for i in range(360):
    ttl.color("cyan")
    ttl.circle(i)
    ttl.lt(5)

done()
