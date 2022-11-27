import turtle   
import time


tut = turtle.Screen()
tut.title("Mathematical Shapes 3d")

# creating a half cicle
tt1 = turtle.Turtle()  
#Providing the colour to be filled  
tt1.color("pink")  
#Instructing to "begin" and "end" filling the "half-circle"  
tt1.begin_fill()  
tt1.circle(90,180)  
tt1.end_fill()  

time.sleep(2)

# drawing a complete circle
#Providing the colour to be filled  
tt1.color("red")    
#Instructing to "begin" and "end" filling the "circle"  
tt1.begin_fill()  
tt1.circle(90)  
tt1.end_fill()  

time.sleep(2)

# drawing a square
#Providing the color to be filled  
tt1.color("yellow")  
  #Instructing to "begin" and "end" filling the "square"  
tt1.begin_fill()  
  #for-loop to run 4 times to complete drawing each side of square  
for j in range(4):  
    tt1.backward(160)  
    tt1.left(90)  
tt1.end_fill()  

time.sleep(2)

# drawing a rectangle
#Providing the color to be filled  
tt1.color("green")  
#Instructing to "begin" and "end" filling the "rectangle"  
tt1.begin_fill()  
#for-loop to run 2 times to complete drawing the sides of rectangle  
for j in range(2):  
    tt1.forward(160)  
    tt1.right(90)  
    tt1.forward(80)  
    tt1.right(90)  
tt1.end_fill()  

time.sleep(2)

# drawing a triangle
tt1.color("blue")  
#Instructing to "begin" and "end" filling the "triangle"  
tt1.begin_fill()  
#for-loop to run 3 times to complete drawing all sides of triangle  
for j in range(3):  
    tt1.forward(100)  
    tt1.right(120)  
tt1.end_fill()  

time.sleep(2)

# drawing a star 
tt1.color("magenta")  
#Instructing to "begin" and "end" filling the "star"  
tt1.begin_fill()    
#for-loop to run 5 times to complete drawing a complete star  
for j in range(5):  
    tt1.forward(200)  
    tt1.right(144)  
tt1.end_fill() 


time.sleep(2)

# drawing a benzene
#Providing the color to be filled  
tt1.color("light green")  
  #Instructing to "begin" and "end" filling the "hexagon"  
tt1.begin_fill()  
  #for-loop to run 6 times to complete drawing a complete hexagon  
for j in range(6):  
    tt1.forward(80)  
    tt1.right(60)  
tt1.end_fill()  

time.sleep(2)

# Drawing a Octagone
#Providing the color to be filled  
tt1.color("light blue")   
#Instructing to "begin" and "end" filling the "octagon"  
tt1.begin_fill()  
#for-loop to run 8 times to complete drawing a complete octagon  
for j in range(8):  
    tt1.forward(80)  
    tt1.right(45)  
tt1.end_fill() 

turtle.done()  

