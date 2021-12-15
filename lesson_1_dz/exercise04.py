# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

number = abs(int(input("Ввудите целое положительное число :")))
max = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break