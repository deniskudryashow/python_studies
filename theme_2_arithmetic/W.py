h = int(input())
a = int(input())
b = int(input())
day = 1
distance = 0
while distance < h:   
    distance += a
    if distance >= h:
        print(day)
    else:
        distance -= b
    day += 1

