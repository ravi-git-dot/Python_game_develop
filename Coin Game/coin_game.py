import turtle
import random

score = 0
sea =turtle.Screen()
sea.bgpic('background.gif')
sea.addshape('player1.gif')
sea.addshape('player.gif')
sea.addshape('coin.gif')

hunter = turtle.Turtle()
hunter.shape('player1.gif')
hunter.penup()
hunter.goto(0,-150)

scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.speed(10)
scoreboard.goto(-100, 240)
scoreboard.write('Score : 0', font = ('Couries',27, 'bold'))
scoreboard.hideturtle()

coin = turtle.Turtle()
coin.speed(50)
coin.shape('coin.gif')
coin.penup()
coin.goto(-280,280)

def left():
    hunter.shape('player1.gif')
    hunter.backward(5)

def right():
    hunter.shape('player.gif')
    hunter.forward(5)

turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

def move():
    y = coin.ycor()
    coin.sety(y-3)

while True:
    sea.update()
    move()
    if coin.ycor() < -300:
        x = random.randint(-280, 280)
        coin.goto(x , 300)
    if hunter.distance(coin) < 50:
        #hunter.write('You capture  the coin')
        score = score + 1
        scoreboard.clear()
        scoreboard.write('Score: {}'.format(score),font = ('Courier', 27, 'bold') )
        x = random.randint(-280, 280)
        coin.goto(x , 300)


turtle.done()