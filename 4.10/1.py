#Distance between 2 points
def distance(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d

x1 =1
y1 =2
x2 =4
y2 =6

print (float(distance(x1, y1, x2, y2)))
