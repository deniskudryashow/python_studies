n = int(input())
syn = {}
for i in range(n):
    a, b =  input().split()
    syn[a] = b
    syn[b] = a

word = input()

print(syn[word])

