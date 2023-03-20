# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

array = []
for i in range(int(input("Введите количество элементов N: "))):
    array.append(random.randint(1, 10))
print(array)
x = int(input("Число X: "))
index = [0, x]
for i, v in enumerate(array):
    tmp = x - v
    if tmp < 0:
        tmp = tmp * -1
    if index[1] > tmp:
        index[0] = i
        index[1] = tmp
print(f"-> {index[0]}")
