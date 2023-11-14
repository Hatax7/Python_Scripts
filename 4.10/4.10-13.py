def slope(x1, y1, x2, y2):
    ''' returns the slope of the line through the points(x1,y1) and (x2,y2)'''
    return (y1 - y2) / (x1 - x2)

print(slope(5, 3, 4, 2))
print(slope(1, 2, 3, 2))
print(slope(1, 2, 3, 3))
print(slope(2, 4, 1, 2))

print()

###

def intercept(x1, y1, x2, y2):
    ''' returns the y-intercept of the line through thr points (x1,y1) and (x2,y2)''' 
    return -slope(x1, y1, x2, y2) * x1 + y1

def intercept2(x1, y1, x2, y2):
    ''' returns the y-intercept of the line through thr points (x1,y1) and (x2,y2)''' 
    return -slope(x1, y1, x2, y2) * x2 + y2

print(intercept(1, 6, 3, 12))
print(intercept(6, 1, 1, 6))
print(intercept(4, 6, 12, 8))

print()

print(intercept2(1, 6, 3, 12))
print(intercept2(6, 1, 1, 6))
print(intercept2(4, 6, 12, 8))
