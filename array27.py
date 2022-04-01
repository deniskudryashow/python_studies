arr = list(map(int, input().split()))
n = len(arr)
tracker = 0
for i in range(0,n-1):
    if arr[i] > 0 and arr[i+1]>0 or arr[i] < 0 and arr[i+1] < 0:
        print (i+1)
        break
    tracker += 1
    if tracker == n:
        print (0)
        