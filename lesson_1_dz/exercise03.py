# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = input("Введите целое число : ")

if not number_n.isdigit():
    print("Unknown format, sorry!")
    exit()

number_n_two = int(number_n + number_n)
number_n_three = int(number_n + number_n + number_n)
summa = int(number_n) + number_n_two + number_n_three
print(summa)