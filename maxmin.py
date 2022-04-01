arr = list(map(int, input().split()))
n = len(arr)
maximum = arr[0]
minimum = arr[0]
for i in range(1,n):
    if maximum < arr[i]:
        maximum = arr[i]
    if minimum > arr[i]:
        minimum = arr[i]
   


    

print(arr)
print( maximum )
print (minimum)
print (type(arr[0]))