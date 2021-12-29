# 3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    if a >= b >= c:
        return a + b
    elif b >= a <= c:
        return b + c
    elif a >= b <= c:
        return a + c
    else:
        print("Неверный формат")


num_1 = int(input("Введите  три числа,\nпервое число >>> "))
num_2 = int(input("второе число >>> "))
num_3 = int(input("третье число >>> "))

print("Сумму двух наибольших чисел >>> ", my_func(num_1, num_2, num_3))

