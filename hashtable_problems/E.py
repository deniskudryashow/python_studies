n, m = map(int, input().split())
Anya_set = set()
Borya_set = set()
for _ in range(n):
    Anya_set.add(int(input()))

for _ in range(m):
    Borya_set.add(int(input()))

Cross = sorted(set(Anya_set & Borya_set))
print(len(Cross))
print(Cross)

Anya_unique = sorted(Anya_set.difference(Cross))
print(len(Anya_unique))
print(Anya_unique)

Borya_unique = sorted(Borya_set.difference(Cross))
print(len(Borya_unique))
print(Borya_unique)


