from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.screensize(canvwidth=800,canvheight=600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)


paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))

ball = Ball()

score_l=Score()

screen.listen()
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s")

screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")

game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()




    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()

    if ball.distance(paddle_r)<50 and ball.xcor()>340 or ball.distance(paddle_l)<50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.reset_position()
        score_l.left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score_l.right_score()






screen.exitonclick()