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