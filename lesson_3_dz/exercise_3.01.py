# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_div(arg_1, arg_2):
    try:
        return round(arg_1 / arg_2, 2)
    except ZeroDivisionError:
        return 0.0


a = int(input("Введите делимое :"))
b = int(input("Введите делитель :"))

print("Результат : ", my_div(a, b))