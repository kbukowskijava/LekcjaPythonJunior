from turtle import *

window = Screen()
reset()

temp = 80

shape("turtle")
bgcolor("green")
color("white")

speed(200)
pensize(3)
circle(temp)

#rysowanie kwadratu
for i in range(4):
    forward(temp / 2)
    right(90)
    forward(temp / 2)

window.exitonclick()
