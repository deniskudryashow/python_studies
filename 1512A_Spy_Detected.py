t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = len(arr)
    for j in range(0,m):
        if arr[j] == arr[j+1]:
            continue
        else:
            if arr[j] !=arr[j+1] and arr[j] == arr[j-1]:
                print(j+1+1)
                break
            else:
                print(j+1)
                break
