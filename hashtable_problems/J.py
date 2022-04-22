n, k = map(int, input().split())
strikes = set()
for i in range(k):  
    a, b = map(int, input().split())
    strikes |= (set([j for j in range(a, n + 1, b)]))

daysoff = set([i for i in range(6, n + 1, 7)]) | set([i for i in range(7, n + 1, 7)])
print(len(strikes - daysoff))

# daysoff = set()
# for m in range(0, int(n/7)):
#     daysoff.add(6 + m*7)
#     daysoff.add(7 + m*7)
# print(strikes)
# print(daysoff)

# print(len(strikes - daysoff))


        

