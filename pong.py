import turtle
import random
import os

wn = turtle.Screen()
wn.title('Pong by Oscar and Crystal')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

def startGame():
    gameStarted = False
  
    wn = turtle.Screen()
    wn.clear()
    wn.title('Pong by Oscar and Crystal')
    wn.bgcolor('black')
    wn.setup(width=800, height=600)
    wn.tracer(0)
    mainMenu.clear()
    #Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.penup()
    paddle_a.goto(-350, 0)
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)

    #Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.penup()
    paddle_b.goto(350, 0)
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)


    randX = random.randrange(-5,5,3)
    randY = random.randrange(-5,5,2)

    #Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = randX
    ball.dy = randY


    #Function
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        if ((y + 50) >= 300) == False:
            paddle_a.sety(y)


    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        if ((y-50)  <= -300) == False:
            paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        y += 20
        if ((y + 50)  >= 300) == False:
            paddle_b.sety(y)


    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        if ((y - 50) <= -300) == False:
            paddle_b.sety(y)

    # Scores
    player1 = 0
    player2 = 0
    
    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)

    wn.onkeypress(paddle_a_up,'w')
    wn.onkeypress(paddle_a_down,'s')

    wn.onkeypress(paddle_b_up,'Up')
    wn.onkeypress(paddle_b_down,'Down')



    #Main Game Loop
    gamePlaying = True
    while gamePlaying:
        wn.update()

        pen.clear()
        pen.write(f'Player 1: {player1}    Player 2: {player2}', align='center', font=('Courier',24,'normal'))


        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            randX = random.randrange(-5,5,3)
            randY = random.randrange(-5,5,2)
            ball.dx = randX
            ball.dy = randY
            player1 += 1

        if  ball.xcor() < -390:
            ball.goto(0, 0)
            randX = random.randrange(-5,5,3)
            randY = random.randrange(-5,5,2)
            ball.dx = randX
            ball.dy = randY
            player2 += 1


        # Paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1


        if player1 == 5 or player2 == 5:
            gamePlaying = False        



    # Pen
mainMenu = turtle.Turtle()
mainMenu.speed(0)
mainMenu.color('white')
mainMenu.penup()
mainMenu.hideturtle()
mainMenu.goto(0, 0)
mainMenu.write('Welcome To Pong, Press The Space Key to Begin',align='center',font=('Courier',28,'bold'))
wn.listen()
wn.onkeypress(startGame,'space')
mainMenu.clear()
gameStarted = True
while gameStarted:
    mainMenu.write('Welcome To Pong, Press The Space Key to Begin\n',align='center',font=('Courier',28,'bold'))
    for i in range(4):
        if i == 0:
            mainMenu.write('|',align='center',font=('Courier',28,'bold'))
        if i == 1:
            mainMenu.write('/')
        if i == 2:
            mainMenu.write('--',align='center',font=('Courier',28,'bold'))
        if i == 3:
            mainMenu.write('\\',align='center',font=('Courier',28,'bold'))

    mainMenu.clear()
    



