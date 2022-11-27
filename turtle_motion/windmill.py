import turtle

t = turtle.Turtle()
colors = ['red', 'blue', 'orange', 'green', 'black', 'brown']

t.speed(0)

for i in range(100):
    t.color(colors[i%6])
    t.begin_fill()
    t.forward(200)
    t.right(120)
    t.forward(40)
    t.end_fill()
    t.goto(0,0)
    t.left(84)

turtle.done()