def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(8))
print(is_even(9))
print(is_even(1))

print()

###

def is_odd(n):
    return not(is_even(n))

print(is_odd(4))
print(is_odd(8))
print(is_odd(9))
print(is_odd(1))
