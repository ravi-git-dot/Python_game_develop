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
space.addshape('left-rocket.gif')
space.addshape('right-rocket.gif')
rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(1000)
def up():
    rocket.setheading(90)
    rocket.shape('rocket.gif')
    rocket.forward(10)
    rocket.setheading(0)

def down():
    rocket.setheading(270)
    rocket.shape('rocket.gif')
    rocket.forward(10)
    rocket.setheading(0)

def left():
    rocket.setheading(180)
    rocket.shape('left-rocket.gif')
    rocket.forward(10)
    rocket.setheading(0)

def right():
    rocket.shape('right-rocket.gif')
    rocket.forward(10)

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