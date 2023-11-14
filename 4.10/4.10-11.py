def compare(a,b):
    if a > b:
        return int(a > b)
    elif a == b:
        return int(a - b)
    else:
        return -(int(a < b))

print(compare(5, 4) == 1)
print(compare(7, 7) == 0)
print(compare(2, 3) == -1)
print(compare(42, 1) == 1)
