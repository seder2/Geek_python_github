# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город
# проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def my_list(name, surname, dob, town, email, phone):
    print(f"name - {name}; "
          f"surname - {surname}; "
          f"day off birthday - {dob}; "
          f"town - {town}; "
          f"email - {email}; "
          f"phone - {phone}"
          )


user_surname = input("Введите фамилию: ")
user_name = input("Введите имя:")
user_dob = int(input("Введите год рождения:"))
user_town = input("Введите город проживания:")
user_email = input("Введите email:")
user_phone = int(input("Введите номер телефона:"))


my_list(
    surname=user_surname,
    name=user_name,
    dob=user_dob,
    town=user_town,
    email=user_email,
    phone=user_phone
)
