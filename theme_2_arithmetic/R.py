minutes = 9*60
n = int(input())
for i in range(1,n):
    if i % 2 == 0:
        minutes +=60
    else:
        minutes +=50
minutes += 45
print(minutes // 60, minutes % 60)