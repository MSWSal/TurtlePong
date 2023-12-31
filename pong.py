import turtle

turtle.setup(400,300)
turtle.bgcolor("black")

#Lpad
Lpad = turtle.Turtle()
Lpad.shape("square")
Lpad.color("red")
Lpad.shapesize(stretch_wid=5, stretch_len=1)
Lpad.penup()
Lpad.goto(-350, 0)
Lpad.dy = 0

#Rpad
Rpad = turtle.Turtle()
Rpad.shape("square")
Rpad.color("yellow")
Rpad.shapesize(stretch_wid=5, stretch_len=1)
Rpad.penup()
Rpad.goto(350, 0)
Rpad.dy = 0

#Ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Rules
gameover =False
winner = None
points = {
    "p1":0,
    "p2":0
}
gamerules ={
    "maxpoints": 3,
    "ballspeed":3
}

#ScoreCard
scoredisplay = turtle.Turtle
scoredisplay.color="white"
scoredisplay.penup()
scoredisplay.hideturtle()
scoredisplay.goto(0, 260)
scoredisplay.write("Player 1: 0 Player 2: 0", align="center", font=("Arial", 24, "normal"))


Lpad.sety(Lpad.ycor() + Lpad.dy)
Rpad.sety(Rpad.ycor() + Rpad.dy)

ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

#check whether game over conditions occured

if points["p1"] == gamerules["maxpoints"]:
    gameover=True
    winner="p1"
elif points["p2"] == gamerules["maxpoints"]:
    gameover=True
    winner="p2"

#check collisions 

if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < Rpad.ycor() +50 and ball.ycor() > Rpad.ycor() -50):
    ball.setx(340)
    ball.dx *= -1
elif(ball.xcor()<-340 and ball.xcor()> -350) and (ball.ycor() < Lpad.ycor() +50 and ball.ycor() > Lpad.ycor() -50):
    ball.setx(-340)
    ball.dx *= -1


#offscreen ball
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["p1"] +=1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["p2"] +=1

#top and bottom collisions

if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *=-1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *=-1

#Update score display
scoredisplay.clear()
scoredisplay.write("Player 1: {}  Player 2: {}".format(points["p1"],points["p1"]),align="center", font=("Arial", 24, "normal"))

#paddle movement defs

def Lpadup():
    Lpad.dy = 10

def Lpaddown():
    Lpad.dy = -10

def Rpadup():
    Rpad.dy = 10

def Rpaddown():
    Rpad.dy = -10

turtle.listen()
turtle.onkeypress(Lpadup,"w")
turtle.onkeypress(Lpaddown,"s")
turtle.onkeypress(Rpadup,"Up")
turtle.onkeypress(Rpaddown, "Down")

#Game over

gameoverdisplay = turtle.Turtle()
gameoverdisplay.color("white")
gameoverdisplay.penup()
gameoverdisplay.hideturtle()
gameoverdisplay.goto(0, 0)
gameoverdisplay.write("Game Over!! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))
