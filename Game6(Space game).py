import turtle
import random
import math
Score = 0

#to create a screen 
scr = turtle.Screen()
scr.title("Space game by pickmycareer")
scr.bgcolor("blue")
scr.bgpic("giphy.gif")
scr.setup(600,800)
scr.tracer(0)  # instally do not show the setups

scr.register_shape("player2.gif")
scr.register_shape("enemy-1.gif")

#to create player
player = turtle.Turtle()
player.shape("player2.gif")
player.penup()
player.goto(0,-355)

#to create enemies
enemies = []
no_of_enemies = 5
for i  in range(no_of_enemies):
    enemy = turtle.Turtle()
    enemy.shape("enemy-1.gif")
    enemy.penup()
    x = random.randint(-220,220)
    y = random.randint(120,345)
    enemy.goto(x,y)
    enemies.append(enemy)
    enemyspeed = 0.1

# to create bullet

bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.shapesize(0.6)
bullet.penup()
bullet.goto(0,-340)
bullet.setheading(90)
bulletspeed = 1
bulletstate = "ready"
bullet.hideturtle()
#ready - ready to shoot
#fire - bullet is moveing

# to create score card

pen = turtle.Turtle()
pen.color("yellow")
pen.penup()
pen.goto(0,375)
pen.write("Score : 0", align = "center", font = ("arial",16,"bold"))
pen.hideturtle()

#to create move with left and right

def player_left():
    x = player.xcor() # to find the current position of x
    x -= 20           # to set increase value for x 
    if x < - 225:     # to limit the x coridnate position
        x = -225
    player.setx(x)    # to set the changes value of x ot the player


def player_right():
    x = player.xcor()
    x += 20
    if x >  225:
        x = 225
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
            bulletstate = "fire"
            bullet.showturtle()
            x = player.xcor()
            y = player.ycor() + 10
            bullet.goto(x,y)

def iscollision(t1,t2):
    distance = math.sqrt((math.pow(t1.xcor()- t2.xcor(),2)) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#to binding on keyboard
scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right,"Right")
scr.onkeypress(fire_bullet, "space")

while True:
    scr.update() # is there any update then show
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 225:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed*= -1
        if enemy.xcor() < -225:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed*= -1
        if iscollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.goto(0,-400)
            x = random.randint(-220,220)
            y = random.randint(120,345)
            enemy.goto(x,y)
            Score += 10
            pen.clear()
            pen.write("Score : {}".format(Score),align = "center", font =("arial", 18 , "bold"))

        if iscollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            exit()
            
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bullet.ycor() > 365:
        bullet.hideturtle()
        bulletstate = "ready"

    


        
        
        


