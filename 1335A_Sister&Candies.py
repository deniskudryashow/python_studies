t = int(input())
for i in range(t):
    n = int(input())
    if  n%2 == 0:
        count =  int((n/2)-1)
    else:
        count = int(n/2)
    print(count)
