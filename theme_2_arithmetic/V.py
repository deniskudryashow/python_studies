n = int(input())
k = int(input())
if k % n == 0:
    print(k % n)
elif k > n:
    print(n - (k % n))

else:
    print(n-k)