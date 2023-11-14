#Calculates hrs mins and secs into total secs
def to_sec(hrs, mins, secs):
    return int(hrs * 3600 + mins * 60 + secs)
def to_sec2(hrs, mins, secs):
    return (hrs * 3600 + mins * 60 + secs) - (hrs * 3600 + mins * 60 + secs) % 1

hrs = 2.5
mins = 0
secs = 10.71

print(to_sec(hrs, mins, secs))
print()
print(to_sec2(hrs, mins, secs))

### Calculates the amount of hrs mins and secs in total secs

def hours_in(secs):
    return secs // 3600

def minutes_in(secs):
    return secs % 3600 // 60

def seconds_in(secs):
    return secs % 3600 % 60 // 1

s = 9010

print(hours_in(s) == 2)
print(minutes_in(s) == 30)
print(seconds_in(s) == 10)
