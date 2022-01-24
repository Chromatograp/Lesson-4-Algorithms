import timeit
import sys

print('Задание 2.')

# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов. Первый — с помощью алгоритма «Решето Эратосфена». Примечание. Алгоритм «Решето Эратосфена» разбирался
# на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу. Второй — без
# использования «Решета Эратосфена». Примечание. Вспомните классический способ проверки числа на простоту.

# Переменные задаем сразу, чтобы счетчик времени не учитывал время ввода переменных пользователем:
n = 100
index = 3


# В каждом алгоритме получаем список простых чисел до числа n. Переменная index нужна для обозначения конкретного
# элемента по счету из полученного списка:
def Sieve_1(n, index):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    a = list(a)
    return a[index - 1]


def Sieve_2(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
            return [i for i in sieve if i != 0]


# Результат вычислений счетчика определяем в переменные, которые затем сравниваем:
way_1 = float(timeit.timeit('Sieve_1(n, index)', number=1000, globals=globals()))
way_2 = float(timeit.timeit('Sieve_2(n)', number=1000, globals=globals()))

# Сравниваем два алгоритма:
if way_1 < way_2:
    print(f'Алгоритм 1, время {way_1} секунд, алгоритм 2, время {way_2} секунд. Первый алгоритм лучше.')
else:
    print(f'Алгоритм 1, время {way_1} секунд, алгоритм 2, время {way_2} секунд. Второй алгоритм лучше.')


def Size(x, level=0):
    print('\t' * level, f'object={x}, type={x.__class__}, size={sys.getsizeof(x)}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                Size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                Size(xx, level + 1)


size_1 = Size(n)
size_2 = Size(index)
size_3 = Size(way_1)
size_4 = Size(way_2)
print(f'{size_1}\n{size_2}\n{size_3}\n{size_4}')