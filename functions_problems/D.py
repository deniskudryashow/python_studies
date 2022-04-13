def isPointinSquare(x,y):
    return bool(abs(x) + abs(y) <= 1)

x = float(input())
y = float(input())

if isPointinSquare(x,y) == True:
    print("YES")
else:
    print("NO")