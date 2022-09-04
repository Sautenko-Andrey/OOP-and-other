import turtle

turtle.showturtle()
turtle.goto(50,50)
if turtle.xcor()>40 or turtle.ycor()>80:
    turtle.goto(0,0)
turtle.goto(50,0)
if turtle.xcor()>40 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(50,-50)
if turtle.xcor()>40 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(0,-50)
if turtle.xcor()==0 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(-50,-50)
if turtle.xcor()<0 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(-50,0)
if turtle.xcor()<0 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(-50,50)
if turtle.xcor()<0 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(0,50)
if turtle.xcor()==0 or turtle.ycor()>80:
    turtle.goto(0, 0)
turtle.goto(0,-50)
if turtle.heading()>=45 and turtle.heading()<=270:
    turtle.setheading(45)
if turtle.isdown():
    turtle.penup()
turtle.goto(100,0)
turtle.pendown()
if turtle.isvisible():
    turtle.hideturtle()
turtle.showturtle()
if turtle.pencolor()=="black":
    turtle.pencolor("red")
turtle.goto(150,0)
if turtle.fillcolor()=="white":
    turtle.fillcolor("black")
if turtle.bgcolor()=="white":
    turtle.bgcolor("grey")
if turtle.pensize()<3:
    turtle.pensize(3)
turtle.goto(0,100)
if turtle.speed()>1:
    turtle.speed(1)
turtle.goto(-100,0)





turtle.done()