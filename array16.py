arr = list(map(int, input().split()))
n = len(arr)
if n % 2 == 0:
    for i in range(1,int((n/2)+1)):
        print (arr[i-1])
        print (arr[-i])
if n % 2 == 1:
    for j in range(1, int((n/2)+1)):
        print (arr[j-1])
        print (arr[-j])
    print(arr[int(n/2)])