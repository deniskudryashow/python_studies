n = int(input())
dict = {}
for i in range(n):
    name = list(input().split())
    for city in name[1:]:
        dict[city] = name[0]
        
m = int(input())
for j in range(m):
    print(dict[input()])
      