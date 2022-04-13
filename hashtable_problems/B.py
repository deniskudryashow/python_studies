# n = list(map(int, input().split()))
# m = list(map(int, input().split()))
# cnt = 0
# for i in range(len(n)):
#     if n[i] in m:
#         cnt += 1
# print(cnt)

n = set(input().split())
m = set(input().split())
l = n | m
print(len(l))