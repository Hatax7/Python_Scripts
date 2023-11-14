import math

def area_of_circle(r):
    print(math.pi * r ** 2)
    print(str(r ** 2) + '*pi')

r = float(input('give radius :'))
area_of_circle(r)
