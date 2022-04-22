from math import sqrt
from re import I
n = int(input())
m = int(sqrt(n))
def MinDivisor(n):
    if n % 2 == 0:
        return 2
    else:
        for i in range(3,m+1,2):
            if n % i == 0:
                return i
        else:
            return n

print(MinDivisor(n))
