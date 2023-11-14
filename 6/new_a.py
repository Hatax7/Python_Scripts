import numpy as np

a = np.array([230,10,284,39,76])
new_a = []
'''
for x in a:
    if x >= 100:
        new_a.append(x)
    else:
        new_a.append(x*2)
a = np.array(new_a)
print(a)
'''
new_a  = []

for x in a:
    while x < 100:
        new_a = []
        for x in a:
            if x >= 100:
                new_a.append(x)
            else:
                new_a.append(x*2)
        a = np.array(new_a)
print(a)
print()

a = np.array([230,10,284,39,76])
new_a = []
temp = 0

for x in a:
    temp = x
    while temp < 100:
        temp = temp * 2
    new_a.append(temp)

a = np.array(new_a)
print(a)
print()

a = np.array([230,10,284,39,76])
new_a = []
temp = 0

for i,x in enumerate(a):
    temp = a[i]
    if temp >=100:
        new_a.append(a[i])
    else:
        while temp < 100:
            temp = temp * 2
        new_a.append(temp)

a = np.array(new_a)
print(a)

for x in a:
    if x>150 and x<200:
        print(x)

print()


            
