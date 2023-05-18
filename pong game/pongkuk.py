#window
import turtle as t
import winsound
wn=t.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#player name
player_a=input("enter player1 name:\n")
player_b=input("enter player2 name:\n")

#score
score_a=0
score_b=0

#paddleA
paddle_a=t.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=7,stretch_len=1)
paddle_a.color("yellow")
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddleB
paddle_b=t.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=7,stretch_len=1)
paddle_b.color("yellow")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=t.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(5)
ball.penup()
ball.goto(0,0)

#pen
pen=t.Turtle()
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle
pen.write("{}:{}  {}:{}".format(player_a,score_a,player_b,score_b),align="center",font=("courier",24,"normal"))
          
#ball moving
ball.dx=1
ball.dy=1

#paddlemove
def paddle_a_up():
    y=paddle_a.ycor()
    y+=30
    if y>=230:
        y=230
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=30
    if y<=-230:
        y=-230
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    if y>=230:
        y=230
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    if y<=-230:
        y=-230
    paddle_b.sety(y)

#keyboradbinding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.xcor()>=390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("{}:{}  {}:{}".format(player_a,score_a,player_b,score_b),align="center",font=("courier",24,"normal"))
        winsound.PlaySound("hit2.wav",winsound.SND_ASYNC)
    if ball.xcor()<=-390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("{}:{} {}:{}".format(player_a,score_a,player_b,score_b),align="center",font=("courier",24,"normal"))
        winsound.PlaySound("hit2.wav",winsound.SND_ASYNC)
                  
    if ball.ycor()>=290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
    if ball.ycor()<=-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    #paddle touch

    if(ball.xcor()>=330 and ball.xcor()<350 and ball.ycor()<(paddle_b.ycor()+70) and ball.ycor()>(paddle_b.ycor()-70)):
        ball.setx(330)
        ball.dx*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
    if(ball.xcor()<=-330 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor()+70 and ball.ycor()>paddle_a.ycor()-70):
        ball.setx(-330)
        ball.dx*=-1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
    










    
    
