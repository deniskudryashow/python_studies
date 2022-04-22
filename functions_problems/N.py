# По данным числам n и k (0≤k≤n) вычислите Сkn. Для решения используйте рекуррентное соотношение Ckn=Ck−1n−1+Ckn−1.
# Решение оформите в виде функции C(n, k).

# Входные данные
# Вводятся целые числа n и k.

# Выходные данные
# Выведите ответ на задачу.

n = int(input())
k = int(input())

def CizNpoK(n,k):
    if k == n or k == 0:
        return 1
    if k != 1: 
        return CizNpoK(n-1,k-1) + CizNpoK(n-1,k)
    return n

print(CizNpoK(n,k))
    
