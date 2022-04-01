n = int(input())
s = str(input())
color = list(s)
cnt = 0
for i in range(n-1):
    if color[i] == color[i+1]:
        cnt += 1
print(cnt)        