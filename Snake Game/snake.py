import turtle
import random

segement = []
grass = turtle.Screen()
grass.bgpic('grass.gif')
grass.addshape('head up.gif')
grass.addshape('head down.gif')
grass.addshape('head right.gif')
grass.addshape('head left.gif')
grass.addshape('body.gif')

# Snake built
snake = turtle.Turtle()
snake.penup()
snake.goto(0, 0)
snake.setheading(90)
snake.shape('head up.gif')

# Food creation
food = turtle.Turtle()
food.penup()
food.shape('circle')
food.color('red')
food.speed(500)
food.goto(100, 10)

# Score screen
pen = turtle.Turtle()
pen.penup()
pen.speed(300)
pen.hideturtle()
pen.goto(0,250)
pen.write('Score : 0', font = ('Courier', 27, 'bold'))

# Snake movement
def move():
    snake.forward(5)

def up():
    if snake.heading() != 270:
        snake.setheading(90)
        snake.shape('head up.gif')

def down():
    if snake.heading() != 90:
        snake.setheading(270)
        snake.shape('head down.gif')

def right():
    if snake.heading() != 180:
        snake.setheading(0)
        snake.shape('head right.gif')

def left():
    if snake.heading() != 0:
        snake.setheading(180)
        snake.shape('head left.gif')

# Key bindings
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

score = 0
# Start program
while True:
    grass.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290 :
        grass.bgpic('game_over.gif')
        food.hideturtle()

    for i in segement:
        if i.distance(snake) < 400:
            grass.bgpic('game_over.gif')
            food.hideturtle()

    if snake.distance(food) < 5:
        x = random.randint(-285,285)
        y = random.randint(-285,285)
        food.setpos(x,y)
        score += 1
        pen.clear()
        pen.write('Score : {}'.format(score), font = ('Courier',27,'bold'))

        # Body creation
        body = turtle.Turtle()
        body.shape('body.gif')
        body.penup()
        body.speed()
        segement.append(body)
    
    for i in range(len(segement)-1, 0, -1):
        x = segement[i - 1].xcor()
        y = segement[i - 1].ycor()
        segement[i].goto(x,y)

    if len(segement) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segement[0].goto(x,y)
    move()   

