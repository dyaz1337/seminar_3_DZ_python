# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

def user_data(first_name, second_name, year_birth, city,
              email, phone_number):
    return f"{first_name} {second_name} {year_birth} года рождения, " \
           f"проживает в городе {city}, " \
           f"email: {email}, телефон: {phone_number}"

try:
    print(user_data(first_name = input("Введите имя:"),
                    second_name = input("Введите фамилию: "),
                    year_birth = int(input("Введите год рождения: ")),
                    city = input("Введите город проживания: "),
                    email = input("Введите ваш email: "),
                    phone_number = int(input("Введите ваш телефон: "))))
except ValueError:
    print("Введите правильные данные!")