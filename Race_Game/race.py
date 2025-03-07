import turtle

# Race background
race = turtle.Screen()
race.bgpic("Race.gif")
race.addshape("Red_car.gif")
race.addshape("Blue_car.gif")

# Create cars
redcar = turtle.Turtle()
redcar.setheading(90)
redcar.penup()
redcar.goto(-100, -240)
redcar.shape("Red_car.gif")

bluecar = turtle.Turtle()
bluecar.setheading(90)
bluecar.penup()
bluecar.goto(100, -240)
bluecar.shape("Blue_car.gif")

# Move the cars
def player1():
    bluecar.forward(3)

def player2():
    redcar.forward(3)

# Key bindings

turtle.onkeypress(player1, "Up")
turtle.onkeypress(player2, "r")
turtle.listen()

# Check if a car has won
while True:
    race.update()
    if redcar.pos() > (-100,200):
        race.bgpic("Red_car_wins.gif")
    if bluecar.pos() > (100,200):
        race.bgpic("Blue_car_wins.gif")

turtle.done()
