def is_factor(x, y):
    return y % x == 0

def is_multiple(x, y):
    return x % y == 0

print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7,14))
print(not is_factor(7, 15))
print(is_factor(1, 15))
print(is_factor(15, 15))
print(not is_factor(25, 15))

print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(not is_multiple(12, 5))
print(is_multiple(12, 6))
print(not is_multiple(12, 7))
