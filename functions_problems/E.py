x = float(input())
y = float(input())
x_c = float(input())
y_c = float(input())
r = float(input())

def isPointInCircle(x, y, x_c, y_c, r):
    return (x < x_c + r and y < y_c + r)

if isPointInCircle(x,y,x_c,y_c,r):
    print("YES")
else:
    print("NO")