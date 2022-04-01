n = int(input())
passanger = list()
for i in range (n):
    a, b  = map(int, input().split())
    station = tuple((a,b))
    passanger.append(station)
tram_capacity = 0
passanger_leave = [x[0] for x in passanger]
passanger_enter = [y[1] for y in passanger]
tram_capacities = []

for k in range(1,n-1):
    tram_capacity = ((((passanger_enter[k-1]-passanger_leave[k])+passanger_enter[k])-passanger_leave[k+1])+passanger_enter[k+1])
    tram_capacities.append(tram_capacity)

m = len(tram_capacities)
minimum = tram_capacities[0]
for j in range(m):
    if minimum < tram_capacities[j] and tram_capacities[j] >= 0:
        minimum = tram_capacities[j]
print(minimum)
print(tram_capacities)
