import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')

arrow = turtle.Turtle()
arrow.color('Hotpink')
arrow.speed(0)

num = 35
size = 20

for x in range(num):
    for x in range(4):
        arrow.forward(size)
        arrow.left(90)
    arrow.penup()
    arrow.left(90)
    arrow.forward(-10)
    arrow.right(90)
    arrow.forward(-10)
    arrow.pendown()
    size += 20

screen.mainloop()
