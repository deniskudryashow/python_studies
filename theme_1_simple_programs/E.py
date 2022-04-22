from math import sqrt
def zeta(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/(i**2)
    return sqrt(sum*6)
print(zeta(10))
