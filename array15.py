
arr = list(map(int, input().split()))
n = len(arr)
for j in range (0, n , 2):
    print (arr[j])

for i in range(n%2, n, 2):
    print(arr[n-i-1])