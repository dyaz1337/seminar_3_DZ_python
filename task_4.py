# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

def my_func_sort(*args):
    args_list = list(args)
    args_list.sort()
    return args_list[-1] + args_list[-2]

def my_func(*args):
    a, b = 0, 0
    args_list = list(args)
    for el in args_list:
        if a < el:
            a = el
        elif b < el:
            b = el
    return a + b

print(my_func_sort(3, 6, 1, 0, 4, 2))
print(my_func(3, 6, 1, 0, 4, 2))

