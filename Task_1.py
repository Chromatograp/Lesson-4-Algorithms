import timeit

print('Задание 1.')

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# минимальны), так и различаться.

# Список задаем программно, чтобы время работы алгоритма не включало ввод списка пользователем:
list = [23, 67, 48, 26, 12, 57, 1, -3, -8, 23]


# Первый алгоритм - через выстраивание чисел по возрастанию и удаление первого по индексу числа:
def Minimum_1(list):
    min1 = []
    list1 = [sorted(list)]
    for i in list1:
        min1.append(i[0:1])
    mini, *min1 = min1
    list_ = list1.pop(0)
    if list_ is not None:
        min2 = [(i[1]) for i in [list_]]
        return *mini, *min2


minimum_1 = float(timeit.timeit('Minimum_1(list)', globals=globals()))


# Второй алгоритм - через срез списка, выстроенного по возрастанию:
def Minimum_2(list):
    return [(i[0:2]) for i in [sorted(list)]]


minimum_2 = float(timeit.timeit('Minimum_2(list)', globals=globals()))


# Третий алгоритм - только с использованием циклов и ветвлений:
def Minimum_3(list):
    if list[0] > list[1]:
        min_ind_1 = 0
        min_ind_2 = 1
    else:
        min_ind_1 = 1
        min_ind_2 = 0
    for i in range(2, len(list)):
        if list[i] < list[min_ind_1]:
            spam = min_ind_1
            min_ind_1 = i
            if list[spam] < list[min_ind_2]:
                min_ind_2 = spam
            elif list[i] < list[min_ind_2]:
                min_ind_2 = i


minimum_3 = float(timeit.timeit('Minimum_3(list)', globals=globals()))

# Сравниваем полученные числа и выявляем наименьшее:
if minimum_1 < minimum_2 < minimum_3 or minimum_1 < minimum_3 < minimum_2:
    print(f'Функция Minimum_1 занимает {minimum_1} секунд - наименьшее количество времени за счет наименьшего количества итераций.')
elif minimum_2 < minimum_1 < minimum_3 or minimum_2 < minimum_3 < minimum_1:
    print(f'Функция Minimum_2 занимает {minimum_2} секунд - наименьшее количество времени за счет наименьшего количества итераций.')
elif minimum_3 < minimum_1 < minimum_2 or minimum_3 < minimum_2 < minimum_1:
    print(f'Функция Minimum_3 занимает {minimum_3} секунд - наименьшее количество времени за счет наименьшего количества итераций.')