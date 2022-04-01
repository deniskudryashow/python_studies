arr = list(map(int, input().split()))
n = len(arr)
bigger = list()
for i in range(1,n,1):
    if arr[i]>arr[i-1]:
        bigger.append(i)
print (bigger)
m = len(bigger)
print (m)
for j in range(m, 0, -1):
    print (bigger[j-1])