pupils = int(input())
l = set()
for i in range (pupils):
        n = int(input())
        a = set()
        for j in range(n):
            a.update({input()})
        l = l & a
print(l)


