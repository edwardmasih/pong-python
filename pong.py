# Simple Pong by @edwardmasih

import turtle

# Window
wn = turtle.Screen()
wn.title("Pong by @edwardmasih")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0\tPlayer B: 0", align="center", font=("Courier", 20, "normal"))

# Functions
def paddle_a_up():
    """to move left paddle up""" #docstring
    y = paddle_a.ycor()
    if paddle_a.ycor() > 220:
        y += 0
        paddle_a.sety(y)
    else:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    """to move left paddle down""" #docstring
    y = paddle_a.ycor()
    if paddle_a.ycor() < -220:
        y += 0
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    """to move right paddle up""" #docstring
    y = paddle_b.ycor()
    if paddle_b.ycor() > 220:
        y += 0
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    """to move right paddle down""" #docstring
    y = paddle_b.ycor()
    if paddle_b.ycor() < -220:
        y += 0
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main Game Loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        # Player A gets point
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}\tPlayer B: {score_b}", align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # ball.setx(390) --> just to check if the ball goes in reverse direction

    if ball.xcor() < -390:
        # Player B gets point
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}\tPlayer B: {score_b}", align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
