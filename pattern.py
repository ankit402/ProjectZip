import random
from turtle import Turtle,Screen

WIDTH =400
HEIGTH=400
color_list=["red", "green", "yellow", "pink", "orange", 'blue', "brown"]
def no_of_turtle():
   count=0
   while True:
         count =(input("How many Turtle want to participate in the race [2:10]"))
         if count.isdigit():
            count = int(count)
         else:
            print("Please input  only numbers [2:10]")
            continue
         if 2<=count<=10:
            return count
         else:
            print("select the input  in between 2 or 10 Try again1!")
turtles= no_of_turtle()
print(turtles)

s1=Screen()
s1.setup(800,800)
x_spacing = WIDTH//turtles+1
turtle_list=[]
for i in range(1,turtles+1):
   new_turtle=Turtle()
   new_turtle.shape("turtle")
   new_turtle.left(90)
   new_turtle.penup()
   new_turtle.color(color_list[i-1])
   new_turtle.goto(-WIDTH//2 + (i*x_spacing), -HEIGTH//2+10)
   turtle_list.append(new_turtle)

def  race():
   is_race_on=True
   while is_race_on:
      for t in turtle_list:
         distance = random.randrange(1, 20)
         t.forward(distance)

         x, y = t.pos()
         if y >= HEIGTH // 2-40:
            print(f"the winner is {t.pencolor()}")
            is_race_on = False


race()
s1.exitonclick()

