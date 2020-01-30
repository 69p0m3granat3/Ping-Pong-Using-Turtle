import turtle

win = turtle.Screen()
win.setup(height=600, width=800)
win.title("Pingpong by Youtube")
win.bgcolor('black')
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1
# Functions


def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


while True:
    win.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy = -0.1

    if ball.ycor() < -290:
        ball.dy = 0.1

    if ball.xcor() > 390:
        ball.dx = -0.1

    if ball.xcor() < -390:
        ball.dx = 0.1
