from turtle import *
speed(20)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(160)
right(90)
forward(60)
right(90)
forward(160)
end_fill()

#roof
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()