arr = list(map(int, input().split()))
n = len(arr)
tracker = 2
for i in range(0,n-1):
    if arr[i]%2 == arr[i+1]%2:
        print (i+1)
        break
    tracker += 1
    if tracker == n:
        print (0)

    
    