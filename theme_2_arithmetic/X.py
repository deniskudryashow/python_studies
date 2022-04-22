n = int(input())
m = str(n)
if m[0] != 0 and m[1] != 0:
    print((n % 1000 - n % 10) + (n % 100 - n % 10 ) + 1) 