import turtle

space = turtle.Screen()
space.bgpic("background.gif")
spaceman = turtle.Turtle()
space.addshape("spaceman.gif")
spaceman.shape("spaceman.gif")
spaceman.penup()
spaceman.goto(-103,255)
rocket = turtle.Turtle()
space.addshape("rocket.gif")
space.addshape('rocket_down.gif')
space.addshape('rocket_left.gif')
space.addshape('rocket_right.gif')
rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(1000)
def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket.gif')

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket_down.gif')

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket_left.gif')

def right():
    rocket.forward(10)
    rocket.shape('rocket_right.gif')

turtle.listen()
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")

while True:
    space.update()
    if rocket.distance(spaceman) < 10 :
        space.bgpic("thankyou.gif")

turtle.done()