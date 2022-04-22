# a = float(input())
# n = int(input())
# result = 1
# def power(a, n):
#     if n >= 0:
#         if n == 0:
#             return int(1)
#         else:
#             result = a*power(a,n-1)
#             n -= 1
#     elif n < 0:
#         if n == 0:
#             return int(1)
#         else:
#             result = (1/a)*power(a, n+1)
#             n += 1
#     return result
        
# print(power(a,n))

from unittest import result


def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result
 
print(power(float(input()), int(input())))