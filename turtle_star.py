from turtle import Turtle,Screen
import random
tom=Turtle()
tom.hideturtle()
s1=Screen()
tom.color("wheat", "yellow")
tom.heading()
tom.speed("fastest")
while True:
    tom.forward(500)
    tom.left(179)

    if tom.heading() ==0:
        break
tom.goto(0,-10)
tom.color('Red')
tom.write("I Love You Urvashi!", font=("Verdana", 12, "bold"))
tom.end_fill()
s1.exitonclick()