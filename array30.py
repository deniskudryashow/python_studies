arr = list(map(int, input().split()))
n = len(arr)
bigger = list()
for i in range(0,n-1,1):
    if arr[i]>arr[i+1]:
        bigger.append(i)
print (bigger)
m = len(bigger)
print (m)
for j in range(m):
    print (bigger[j])