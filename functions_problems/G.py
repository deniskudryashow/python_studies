a = int(input())
n = int(input())
result = 0
def power(a, n):
    if n == 0:
        return int(1)
    else:
        result = a*power(a,n-1)
        n -= 1
    return result
        
print(power(a,n))
