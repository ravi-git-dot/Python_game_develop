#Chitti Logo

import turtle

scr = turtle.Screen()
point = turtle.Turtle()
point.shape("turtle")
point.width(5)

point.penup()
point.goto(-120,45)
point.pendown()
point.fillcolor("Gold")
point.begin_fill()
point.goto(125,45)
point.left(90)
point.forward(65) 

for i in range(180):
    point.forward(2.1)
    point.left(1)

point.forward(65)
point.end_fill()
point.forward(125)

for i in range(180):
    point.forward(2.1)
    point.left(1)

point.forward(125)

#code for Eye
point.width(30)
point.color("black")
point.penup()
point.goto(-60,20)
point.pendown()
point.goto(-60,-30)
point.penup()
point.goto(60,20)
point.pendown()
point.goto(60,-30)
point.penup()
point.goto(-75,-75)
point.pendown()
point.width(8)
point.left(180)

for i in range(180):
    point.forward(1.5)
    point.left(1)
point.hideturtle()

turtle.done()