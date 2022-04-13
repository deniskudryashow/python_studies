from re import L


L = list(map(int, input().split()))
d = {}
for i in range(len(L)):
    if L[i] in d.values():
        print("YES")
    else:
        d[i] = L[i]
        print("NO")

    