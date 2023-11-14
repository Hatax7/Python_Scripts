import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.title('Spiral')

sp = turtle.Turtle()
sp.color('blue')
sp.pensize(5)
sp.speed(0)

def spiral(t,s,a,n):
    for x in range(n):
        t.right(90)
        t.forward(s)
        s += 5
        t.left(a)

size = 5
angle = 1
number = 100

spiral(sp, size, angle, number)
