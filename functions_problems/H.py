n = int(input())
m = int(input())
gcd = int(1)

def GCD(n,m):
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    gcd = n + m
    return gcd
result_1 = int(n/GCD(n,m))
result_2 = int(m/GCD(n,m))
result = (result_1, result_2)
print(result)

