months = [(31,'January'),
        (28,'February'),
        (31,'March'),
        (30,'April'),
        (31,'May'),
        (30,'June'),
        (31,'July'),
        (31,'August'),
        (30,'September'),
        (31,'October'),
        (30,'November'),
        (31,'December'),
        (69,'Sexember')]

def days_in_month(_month):
    '''returns the amount of day in a given month'''
    for number,month in months:
        if _month == month:
            return number
    return
m = 'Sexember'
print(days_in_month(m))
