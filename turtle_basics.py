from turtle import *

WIDTH, HEIGHT = 600,100

bgcolor("black")  
pensize(2)  
speed(10)  

# Screen().screensize(canvwidth=400, canvheight=800, bg=None)
# Screen().setup()
screen = Screen()
screen.setup(800 + 4, 1000 + 8)  # fudge factors due to window borders & title bar
# screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

t1 = Turtle()  

# t1.forward(100)  
# t1.right(25)  
# t1.forward(100)
# t1.left(25) 
# t1.backward(100) 

colors = ["red","yellow","green","blue","grey","red","yellow","green","blue","grey"]
for i in range(10):
    t1.color(colors[i])
    t1.begin_fill()
    t1.circle(50+i*10)
    t1.right(36)
    t1.end_fill()



# # To stop the screen to display  
mainloop()  