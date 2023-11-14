import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.title('Pretty pattern')

sq = turtle.Turtle()
sq.color('blue')
sq.pensize(5)
sq.speed(0)

def square(t,s):
    for x in range(4):
        t.forward(s)
        t.right(90)

#square(sq,200)
size = 200

def shp(t,s):
    for x in range(20):
        square(t,s)
        t.right(360/20)

shp(sq,size)    
