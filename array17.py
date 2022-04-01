arr = list(map(int, input().split()))
n = len(arr)
if n % 2 == 0:
    for i in range(1,int((n/2)+1), 2):
        print (arr[i-1])
        print (arr[i])
        print (arr[-i])
        print (arr[-i-1])
if n % 2 == 1:
    for j in range(1, int((n/2)+1), 2):
        print (arr[j-1])
        print (arr[j])
        print (arr[-j])
        print (arr[-j-1])