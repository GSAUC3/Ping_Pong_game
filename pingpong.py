import turtle

win = turtle.Screen()
win.title("Pingu Pong")
win.bgcolor('yellow')  # background color
win.setup(width=800, height=600)  # size of window
# it actually statrs the window from updating, to spped up the game
win.tracer(0)

# paddle a -----object/graphics creation-----------
pad_a = turtle.Turtle()  # capital Turtle is a class name

pad_a.speed(0)  # speed of animation
pad_a.shape('square')  # default shape is 20x20 pixels
pad_a.color("green")
pad_a.shapesize(stretch_wid=5, stretch_len=1)  # to elongate the paddle a
pad_a.penup()
pad_a.goto(-350, 0)

score = turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0,250)
score.hideturtle()
score.write("Player A: 0    Computer : 0",align="center" ,font=("Helvatica",24,"normal") )




# paddle b------object/graphics creation----------
pad_b = turtle.Turtle()  # capital Turtle is a class name

pad_b.speed(0)  # speed of animation
pad_b.shape('square')  # default shape is 20x20 pixels
pad_b.color("blue")
pad_b.shapesize(stretch_wid=5, stretch_len=1)  # to elongate the paddle a
pad_b.penup()
pad_b.goto(350, 0)

# ball-------------------

ball = turtle.Turtle()  # capital Turtle is a class name

ball.speed()  # speed of animation
ball.shape('circle')  # default shape is 20x20 pixels
ball.color("red")
ball.penup()
ball.goto(0, 0)
dx = 0.3
dy = 0.3

# paddle a movement -------
s_a=0
s_c = 0

def padaup():
    y = pad_a.ycor()  # returns the y cordinate of the object pad_a paddle a
    y += 45
    pad_a.sety(y)


def padadown():
    y = pad_a.ycor()  # returns the y cordinate of the object pad_a paddle a
    y -= 45
    pad_a.sety(y)


# paddle b movement -------
def padbup():
    y = pad_b.ycor()  # returns the y cordinate of the object pad_a paddle a
    y += 1
    pad_b.sety(y)


def padbdown():
    y = pad_b.ycor()  # returns the y cordinate of the object pad_a paddle a
    y -= 1
    pad_b.sety(y)


# key bind --------

win.listen()  # listen for keyboard input
win.onkeypress(padaup, "w")
win.onkeypress(padadown, "s")
#  when w is pressed , padaup function will be called
#  padaup function will be called everytime w is pressed
#  and hence it the y-cordinate will be increased by 20 when w is pressed


bounce = False
# main game loop
while True:
    win.update()  # everytime the loop runs it will update the screen

    # movement of the ball
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
    # set ball position to (previous position +  pix)

    # bouncing off the walls-----

    if ball.ycor() > 290:
        ball.sety(290)  # if the ball touches the top wall
        # then it's ordinate will be set to 290 multiplied by -1 to
        # reverse the direction
        dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        dy *= -1
    # -----------

    # collision and bouncing off the paddle

    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() > pad_a.ycor() - 45) and (pad_a.ycor()+40 > ball.ycor()):
        ball.setx(-340)
        dx *= -1
        bounce = False

 #    ---------- computer move-------------
    if (ball.xcor() < 350 and ball.xcor() > 340) and (ball.ycor() > pad_b.ycor() - 45) and (pad_b.ycor()+40 > ball.ycor()):
        ball.setx(340)
        dx *= -1
        bounce = True

    if (ball.ycor() - pad_b.ycor() > 50) and ball.xcor() < 330 and bounce == False:
        padbup()

    # and ball.xcor() < 300

    if (ball.ycor() - pad_b.ycor() < 50) and ball.xcor() < 330 and bounce == False:
        padbdown()

 # reset ball position when defeted
    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        dx *= -1
        dy *= -1
        s_a+=1
        score.clear()
        score.write("Player A: {}    Computer : {}".format(s_a,s_c),align="center" ,font=("Helvatica",24,"normal") )


    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        dx *= -1
        dy *= -1
        bounce=False
        s_c+=1
        score.clear()

        score.write("Player A: {}    Computer : {}".format(s_a,s_c),align="center" ,font=("Helvatica",24,"normal") )