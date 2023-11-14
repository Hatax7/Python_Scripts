def prime_lessthan(n):
    '''Makes a list of primes lesser than n'''
    primes = []
    counter = 0
    for x in range(2,n):
        for i in range(2,x):
            if x % i == 0:
                counter += 1
                break
        if counter != 0:
            counter =0
            continue
        primes.append(x)
    return primes
print(prime_lessthan(100))

def is_prime(i):
    for x in range(2,i):
        if i % x == 0:
            return False
    return True

def primes_lessthan2(n):
    '''Same as above'''
    result = []
    for i in range(2,n):
        if is_prime(i):
            result.append(i)
    return result
print(primes_lessthan2(100))
print(prime_lessthan(100) == primes_lessthan2(100))
