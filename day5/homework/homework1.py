from turtle import*
speed(10)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

forward(70)
color("blue")
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
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#second house
penup()
goto(-300,0)
pendown()
left(120)  
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

forward(70)
color("green")
begin_fill()
left(90)
forward(160)
right(90)
forward(60)
right(90)
forward(160)
end_fill()

penup()
goto(-100,200) 
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#sun Added everything
speed(1)
penup()
goto(300, 300) 
pendown()
color("yellow")
begin_fill()
circle(50)
end_fill()

#3 house
penup()
goto(-600,0)
pendown()
left(120)  
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

forward(70)
color("purple")
begin_fill()
left(90)
forward(160)
right(90)
forward(60)
right(90)
forward(160)
end_fill()

penup()
goto(-400,200) 
pendown()
color("light green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
