import turtle
import random
import math


score = 0
#to create a screen
scr = turtle.Screen()
scr.title("Space fighter game by pickmycarier")
scr.bgcolor("black")
scr.setup(800,800)
scr.tracer(0)

# to draw the player
player_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
scr.register_shape("player",player_vertices)

#to create a player
player = turtle.Turtle()
player.shape("player")
player.color("white")
player.penup()
player.goto(0,0)

# to draw asteroid stone
asteroid_vertices = ((0,10),(8,5),(3,7),(8,2),(6,5),(7,-5),(0,-9),(-5,-5),(-7,-7),(-9,0),(-6,5),(-2,7))
scr.register_shape("asteroid",asteroid_vertices)

#to create asteriod
def get_heading_to(t1,t2):
    x1 = t1.xcor()
    y1 = t1.ycor()

    x2 = t2.xcor()
    y2 = t2.ycor()

    heading = math.atan2(y1-y2, x1-x2)
    heading = heading*180.0/3.14159
    return heading

asteroids =[]
for i in range(5):
    asteroid = turtle.Turtle()
    asteroid.shape("asteroid")
    asteroid.color("brown")
    asteroid.speed = random.randint(1,10)/1000
    asteroid.penup()
    heading = random.randint(0,360)
    distance = random.randint(400,600)
    asteroid.setheading(heading)
    asteroid.forward(distance)
    asteroid.setheading(get_heading_to(player, asteroid))
    asteroids.append(asteroid)

#to create bullet
missiles = []
for i in range(3):
    missile = turtle.Turtle()
    missile.goto(0,0)
    missile.shape("arrow")
    missile.color("gold")
    missile.penup()
    missile.speed = 0.4
    missile.state = "ready"
    missiles.append(missile)
    missile.showturtle()
        
#to create score board
pen = turtle.Turtle()
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.goto(0,350)
pen.write("Score : 0", align = "center", font =("arial", 22, "bold"))
pen.hideturtle()

#to create rotate left and right
def rotate_left():
    player.left(10)
def rotate_right():
    player.right(10)
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0,0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break

#to binding keyboeard
scr.listen()
scr.onkeypress(rotate_left,"Left")
scr.onkeypress(rotate_right,"Right")
scr.onkeypress(fire_missile,"space")

while True:
    scr.update()
    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        if missile.xcor() > 400 or missile.xcor() <-400  or missile.ycor() > 400 or missile.ycor() < -400:
            missile.hideturtle()
            missile.state = "ready"

        for asteroid in asteroids:
            asteroid.forward(asteroid.speed)
            for missile in missiles:
                if asteroid.distance(missile)<20:
                    heading = random.randint(0,360)
                    distance = random.randint(400,600)
                    asteroid.setheading(heading)
                    asteroid.forward(distance)
                    asteroid.setheading(get_heading_to(player, asteroid))
                    asteroid.speed +=0.01
                    missile.hideturtle()
                    missile.goto(1000,1000)
                    missile.state = "ready"
                    score += 10
                    pen.clear()
                    pen.write("Score : {}".format(score), align = "center", font =("arial", 22, "bold"))

                if asteroid.distance(player) < 20:
                    print ("Player killed")
                    exit()
                    
                    

