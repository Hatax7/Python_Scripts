days = [(0,'Monday'),
        (1,'Tuesday'),
        (2,'Wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
        (69,'Sexday lol')]

def day_add(today,delta):
    '''returns what day you leave on holiday'''
    for number,day in days:
        if today == day:
            t = number
    n = ( t + delta ) % 7
    for number,day in days:
        if number == n:
            return day
delta = -100
today = 'Tuesday'
print(day_add(today,delta))
