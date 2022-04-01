arr = list(map(int, input().split()))
n = len(arr)
odd = list()
for i in range (0, n, 2):
    odd.append(arr[i])
m = len(odd)
maximum = odd[0]
for j in range(m):
    if odd[j] > maximum:
        maximum = odd[j]
print (maximum)