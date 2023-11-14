import turtle
import star

screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.title('star')

s = turtle.Turtle()
s.color('hotpink')
s.pensize(5)
s.speed(0)

l = 100
distance = 350

s.penup()
s.goto(-(distance/2),0)
s.pendown()
for x in range(5):
    s.penup()
    s.forward(distance)
    s.right(144)
    s.pendown()
    star.star(s,l)
