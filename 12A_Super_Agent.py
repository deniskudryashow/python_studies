import re
str = ''
for i in range(3):
    str = str + input()
   
code = list(str)

reversed_code = code.copy()
reversed_code.reverse()
# print(reversed_code)

if code == reversed_code:
    print("YES")
else:
    print("NO")