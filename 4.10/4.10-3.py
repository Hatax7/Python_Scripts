days = [(1,'Monday'),
        (2,'Tuesday'),
        (3,'Wednesday'),
        (4,'Thursday'),
        (5,'Friday'),
        (6,'Saturday'),
        (0,'Sunday'),
        (69,'Sexday lol')]

def day_num(d):
    '''returns day for numbers 0-6'''
    for number,day in days:
        if day == d:
            return number
    return
d = 'Sexday lol'
print(day_num(d))
