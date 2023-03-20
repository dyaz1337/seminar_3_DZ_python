# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

month = int(input("Введите номер месяца: "))
list_months = ['зима', 'весна', 'лето', 'осень']
dict_months = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
if month == 1 or month == 2 or month == 12:
    print(list_months[0])
    print(dict_months.get(1))
elif month == 3 or month == 4 or month == 5:
    print(list_months[1])
    print(dict_months.get(2))
elif month == 6 or month == 7 or month == 8:
    print(list_months[2])
    print(dict_months.get(3))
elif month == 9 or month == 10 or month == 11:
    print(list_months[3])
    print(dict_months.get(4))
else:
    print("Нет такого месяца. Попробуйте снова")