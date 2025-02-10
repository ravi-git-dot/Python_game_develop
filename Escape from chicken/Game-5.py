import turtle
import random

scr= turtle.Screen()
scr.title("Game demo-3")
scr.bgpic("giphy.gif")
scr.setup(400,600)

#register shape
scr.register_shape("player1-min.gif")
scr.register_shape("chicken.gif")

player = turtle.Turtle()
player.shape("player1-min.gif")
player.penup()
player.goto(0,-230)

chick = turtle.Turtle()
chick.shape("chicken.gif")
chick.penup()
x = random.randint(-150, 150)
chick.goto(x,200)

#player move left and right
def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def player_right():
    x = player.xcor()
    x +=20
    player.setx(x)

#keyboard binding

scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right, "Right")

while True:
    y = chick.ycor()
    y -=0.5
    chick.sety(y)

turtle.done()
