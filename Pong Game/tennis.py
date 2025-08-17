import turtle

ground = turtle.Screen()
ground.bgpic('ground.gif')
ground.addshape('left.gif')
ground.addshape('right.gif')
ground.addshape('ball.gif')
ground.title("Tennis Game")

# Heading setup
pen = turtle.Turtle()
pen.hideturtle()           
pen.penup()
pen.color('white')
pen.goto(0, 270)           
pen.write("Tennis Game Graphics", align="center", font=("courier", 24, "bold"))

# LeftPlayer Score
leftpen = turtle.Turtle()
leftpen.hideturtle()           
leftpen.penup()
leftpen.color('white')
leftpen.goto(-450, 220)           
leftpen.write("LeftPlayer Score : 0", font=("Courier", 24, "bold"))

# Rightplayer Score
rightpen = turtle.Turtle()
rightpen.hideturtle()           
rightpen.penup()
rightpen.color('white')
rightpen.goto(50, 220)           
rightpen.write("RightPlayer Score : 0", font=("Courier", 27, "bold"))

#Right Player setup
rightplayer = turtle.Turtle()
rightplayer.penup()
rightplayer.shape('right.gif')
rightplayer.goto(400,-200)

# Left Player setup
leftplayer = turtle.Turtle()
leftplayer.penup()
leftplayer.shape('left.gif')
leftplayer.goto(-400,200)

# Ball setup
ball = turtle.Turtle()
ball.penup()
ball.shape('ball.gif')

# leftplayer movement
def leftplayerup():
    y= leftplayer.ycor()
    leftplayer.sety(y+10)

def leftplayerdown():
    y= leftplayer.ycor()
    leftplayer.sety(y-5)

def leftplayerright():
    x= leftplayer.xcor()
    leftplayer.setx(x+10)

def leftplayerleft():
    x= leftplayer.xcor()
    leftplayer.setx(x-10)

# rightplayer movement
def rightplayerup():
    y= rightplayer.ycor()
    rightplayer.sety(y+10)

def rightplayerdown():
    y= rightplayer.ycor()
    rightplayer.sety(y-5)

def rightplayerright():
    x= rightplayer.xcor()
    rightplayer.setx(x+10)

def rightplayerleft():
    x= rightplayer.xcor()
    rightplayer.setx(x-10)

# Keys
turtle.onkeypress(leftplayerup, 'w')
turtle.onkeypress(leftplayerdown, 's')
turtle.onkeypress(leftplayerright, 'd')
turtle.onkeypress(leftplayerleft, 'a')

turtle.onkeypress(rightplayerup, 'Up')
turtle.onkeypress(rightplayerdown, 'Down')
turtle.onkeypress(rightplayerright, 'Right')
turtle.onkeypress(rightplayerleft, 'Left')
turtle.listen()

dx = 1
dy = -1

leftscore = 0
rightscore = 0

while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x+dx, y+dy) 

    if leftplayer.distance(ball) < 10:
        dx = -dx

    if rightplayer.distance(ball) < 10:
        dx = -dx

    if ball.ycor() > 280:   # top boundary
        dy = -dy

    if ball.ycor() < -280:  # bottom boundary
        dy = -dy


    if ball.xcor() > 450:   # right wall
        ball.goto(0, 0)
        leftpen.clear()
        leftscore += 1
        leftpen.write(("LeftPlayer Score : {}").formate(leftscore), font=("Courier", 24, "bold"))

    if ball.xcor() < -450:  # left wall
        ball.goto(0, 0)
        rightpen.clear()
        rightscore += 1
        rightpen.write(("RightPlayer Score : {}").formate(rightscore), font=("Courier", 27, "bold"))

turtle.done()