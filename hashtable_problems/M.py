dict = {}
for i in range(51):
    candidate, votes = input().split()
    dict[candidate] = dict.get(candidate,0) + int(votes)

for candidate, votes in sorted(dict.items()):
    print(candidate, votes)

