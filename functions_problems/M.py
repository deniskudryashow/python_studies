# Напишите функцию phib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы - используйте рекурсию.

# phib(1) = phib(2) = 1

# .phib(n) = phib(n - 1) + phib(n - 2)

# Входные данные
# Вводится целое число.

# Выходные данные
# Выведите ответ на задачу.




n = int(input())
def phib(n):
    if n <= 2:
        return 1
    return (phib(n-1)+phib(n-2))
print(phib(n))
