import turtle
from turtle import Turtle
import  random
color =["red", "green", "yellow"]
turtle.colormode((255))
tom=Turtle()
tom.width(10)
tom.shape('turtle')
for i in range(3,9):
    angle = 360/i
    for _ in range(i):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        tom.forward(100)
        tom.pencolor(r,g,b)
        tom.right(angle)
tom.screen.mainloop()

