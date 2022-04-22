# Дано натуральное число x>1. Проверьте, является ли оно простым. Программа должна вывести слово YES, если число простое и NO, если число составное.

# Решение оформите в виде функции IsPrime(x), которая возвращает True для простых чисел и False для составных чисел. Решение должно иметь сложность O(x−−√).

# Входные данные
# Вводится натуральное число.

# Выходные данные
# Выведите ответ на задачу.

# x = int(input())

# def isPrime(x):
#     if x == 0 or x == 1:
#         return "NO"
#     for i in range(2, int(x**(1/2))):
#         if x % i == 0:
#             return "NO"
#     return "YES"

# print(isPrime(x))

x = int(input())

def isPrime(x):
    if x <= 3:
        return "YES"
    if not x % 2 or not x % 3:
        return "NO"
    i = 5
    end = int(x**0.5)
    while i <= end:
        if not x % i or not x % (i+2):
            return "NO"
        i += 6
    return "YES"
print(isPrime(x))