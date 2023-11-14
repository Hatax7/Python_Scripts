def f2c(t):
    return round(( t - 32 ) * ( 5 / 9 ) )

def c2f(t):
    return round (t * (9/5) + 32)

nums = [212, 32, -40, 36, 37, 38, 39]

nums2 = [0, 100, -40, 12, 18, -48]

for x in nums:
    print(f2c(x))
    continue
print()
for x in nums2:
    print(c2f(x))
    continue


