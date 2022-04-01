k, n, w  = map(int, input().split())
total_price = 0
for i in range(1,w+1):
    total_price = total_price + (k*i)
    print(total_price)

result = total_price - n

if result < 0:
    print(0)
else:
    print(result)
