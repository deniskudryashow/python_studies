L = list(map(int, input().split()))
s = set()
for i in range(len(L)):
    if L[i] in s:
        print("YES")
    else:
        s.add(L[i])
        print("NO")

    