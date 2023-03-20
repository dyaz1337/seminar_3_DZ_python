# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
# Process finished with exit code 0
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
# Process finished with exit code 0

def divNumbers(*numbers):
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        result = number_1 / number_2
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return result
print(f'result {divNumbers()}')
