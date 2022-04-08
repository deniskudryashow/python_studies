n = int(input())
cnt = 0
for i in range(n):
    arr = list(map(int, input().split()))
    if sum(arr) >= 2:
        cnt += 1
    else:
        continue
print(cnt) 