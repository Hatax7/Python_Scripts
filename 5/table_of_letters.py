string = 'ThiS is String with Upper and lower case Letters'
d = {}
l = list(string)
for x in l:
    d[x.lower()] = d.get(x.lower(),0) + 1
#print(d)
l2 = list(d.items())
l2.sort()
#print(l2)
for k,v in l2:
    print(str(k)+' '+str(v))

d2 = {}
for letter in string:
    d2[letter.lower()] = d2.get(letter.lower(),0) + 1
print(d2)
a = list(d2.items())
a.sort()
for k,v in a:
    print(str(k)+' '+str(v))
print(a == l2)
