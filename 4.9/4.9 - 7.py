def sum_to(n):
    sum = 0
    for x in range(n):
        sum += n
        n -= 1
    print(sum)

n = 10
sum_to(n)


def sum_tov2(i):
    sum = 0
    z = 0
    while z <= i:
        sum += z
        z += 1
    print(sum)

i = 10
sum_tov2(i)
