from fractions import Fraction
y, w = map(int, input().split())
win_chance = 0
if y == w == 1: 
    result = "1/1"
    print(result)
elif y >= w:
    win_chance =  6-(y-1)
    result = (Fraction(win_chance, 6))
    print(result)
else:
    win_chance = 6-(w-1)
    result = (Fraction(win_chance, 6))
    print(result)