def leibnitz(n):
    sum = 0
    for i in range(n):
        element = (-1) ** i/(2*i+1)
        sum = sum + element
    return sum*4

print(leibnitz(10)) 