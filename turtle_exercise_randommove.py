import turtle
from turtle import Turtle
import  random
turtle.colormode(255)
tom= Turtle()
tom.width(10)
tom.speed(10)
tom.shape("turtle")
for i in range(50):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.setheading(random.randrange(0,360,90))
    tom.pencolor(r,g,b)
    tom.forward(30)
tom.screen.mainloop()