from turtle import *

bgcolor("black")

ttl = Turtle()
ttl.speed(0)
colors = ["yellow","red","white","blue","green"]
for i in range(400):
    ttl.color(colors[i%5])
    ttl.pensize(i/10+1)
    ttl.fd(i)
    ttl.left(59)

done()