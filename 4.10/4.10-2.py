days = [(0,'Monday'),
        (1,'Tuesday'),
        (2,'Wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
        (69,'Sexday lol')]

def day_name(n):
    '''returns day for numbers 0-6'''
    for number,day in days:
        if number == n:
            return day
    return
n = 69
print(day_name(n))

###

def day_name2(name):
    '''returns day for numbers0-6'''
    if name == 0:
        return 'Monday'
    elif name == 1:
        return 'Tuesday'
    elif name == 2:
        return 'Wednesday'
    elif name == 3:
        return 'Thursday'
    elif name == 4:
        return 'Friday'
    elif name == 5:
        return 'Saturday'
    elif name == 6:
        return 'Sunday'
    return

name = 1
print(day_name2(name))
