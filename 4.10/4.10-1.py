def turn_clockwise(direction):
    '''gives next compass direction in clockwise manner'''
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'
    return

direction = 'W'
print(turn_clockwise(direction))

###

n = [('W','N'),
     ('N','E'),
      ('E','S'),
      ('S','W')]
      
def turn_clockwise(d):
    '''gives next compass direction in clockwise manner'''
    for given,returned in n:
        if given == d:
            return returned
    return

d = 'E'
print(turn_clockwise(d))
