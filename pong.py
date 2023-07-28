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
gameover =Falsewinner =None
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