# n = int(input())

# Dict1 = {}
# Dict2 = {}

# for i in range(n):
#     arr = list((input().split()))
#     for j in range(len(arr)):
#         Dict1[arr[0]] = arr[j]

# print(Dict1)


# m = int(input())

# for k in range(m):
#     operation_list = list((input().split()))
#     Dict2[operation_list[1]] = operation_list[0]


# for x in Dict2.keys():
#     value1 = Dict1.get(x)
#     value2 = Dict2.get(x, None)
#     if value1 == value2:
#         print('OK')
#     else:
#         print('Access denied')

n = int(input())  
x = {'write':'W','read':'R','execute':'X'}
d={}
for i in range(n):
    a, *b = input().split()
    d[a] = set(b)

print(d)
m = int(input())
for i in range(m):
    a, b = input().split()
    if x[a] in d[b]:
        print(x[a])
        print(d[b])
        print('OK')
    else:
        print('Access denied')
