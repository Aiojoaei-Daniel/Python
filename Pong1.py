
import turtle

da = turtle.Screen()
da.title("Pong")
da.bgcolor("red")
da.setup(width=800, height=600)
da.tracer(0)

# Scor
score_1 = 0
score_2 = 0


# player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("green")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("green")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0      Player 2: 0 ", align="center", font=("Courier", 15, "normal"))

#functii pentru miscare paletelor in sus si in jos


def player1_up():
    y = player1.ycor()
    y += 10
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 10
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 10
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 10
    player2.sety(y)


# apelam functiile de miscare a paletelor

da.listen()
da.onkeypress(player1_up, "w")
da.onkeypress(player1_down, "s")
da.onkeypress(player2_up, "Up")
da.onkeypress(player2_down, "Down")

# main loop

while True:
    da.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)            # xcor = coordonatele curente + dx = 0.1
    ball.sety(ball.ycor() + ball.dy)

    # marginea jocului
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}      Player 2: {} ".format(score_1, score_2), align="center", font=("Courier", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}      Player 2: {} ".format(score_1, score_2), align="center", font=("Courier", 15, "normal"))

    # paletele si mingea // impact
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

