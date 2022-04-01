from asyncio import events


arr = list(map(int, input().split()))
n = len(arr)
even = list()
for i in range (1, n, 2):
    even.append(arr[i])
m = len(even)
minimum = even[0]
for j in range(m):
    if even[j] < minimum:
        minimum = even[j]
print (minimum)
