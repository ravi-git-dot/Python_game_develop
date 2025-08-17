# Batman Logo rotated at an angle
import turtle
import math

# Rotation function
def rotate_point(x, y, angle):
    rad = math.radians(angle)
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return x_new, y_new

#set angle
angle = 45  

pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("black")
pen.begin_fill()
pen.penup()

# Original pattern but with rotation applied
x, y = rotate_point(0,-30, angle)
pen.goto(x, y)
x, y = rotate_point(10,-10, angle)
pen.goto(x, y)
x, y = rotate_point(20,-20, angle)
pen.goto(x, y)
x, y = rotate_point(30,-10, angle)
pen.goto(x, y)
x, y = rotate_point(40,-20, angle)
pen.goto(x, y)
x, y = rotate_point(70,0, angle)
pen.goto(x, y)
x, y = rotate_point(30,30, angle)
pen.goto(x, y)
x, y = rotate_point(10,10, angle)
pen.goto(x, y)
x, y = rotate_point(10,15, angle)
pen.goto(x, y)
x, y = rotate_point(10,30, angle)
pen.goto(x, y)
x, y = rotate_point(5,20, angle)
pen.goto(x, y)
x, y = rotate_point(0,20, angle)
pen.goto(x, y)
x, y = rotate_point(-5,20, angle)
pen.goto(x, y)
x, y = rotate_point(-10,30, angle)
pen.goto(x, y)
x, y = rotate_point(-10,15, angle)
pen.goto(x, y)
x, y = rotate_point(-10,10, angle)
pen.goto(x, y)
x, y = rotate_point(-30,30, angle)
pen.goto(x, y)
x, y = rotate_point(-70,0, angle)
pen.goto(x, y)
x, y = rotate_point(-40,-20, angle)
pen.goto(x, y)
x, y = rotate_point(-30,-10, angle)
pen.goto(x, y)
x, y = rotate_point(-20,-20, angle)
pen.goto(x, y)
x, y = rotate_point(-10,-10, angle)
pen.goto(x, y)
x, y = rotate_point(0,-30, angle)
pen.goto(x, y)

pen.end_fill()
pen.hideturtle()
turtle.done()
