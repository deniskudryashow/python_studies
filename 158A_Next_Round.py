n, k = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] >= arr[k-1] and arr[i] > 0:
        cnt += 1
print(cnt)
    