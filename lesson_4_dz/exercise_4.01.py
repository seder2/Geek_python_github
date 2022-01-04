# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах*ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

if len(argv) == 4:
    file, work_time, rate, bonus = argv
    work_time = float(work_time)
    rate = float(rate)
    bonus = float(bonus)
    print(f"Размер заработной платы составил: {work_time * rate + bonus}")
else:
    work_time = float(input("Введите количество отработанных часов : "))
    rate = float(input("Введите суммы оплаты труда за 1 час : "))
    bonus = float(input("Укажите размер премии -  "))
    print(f"Размер заработной платы составил: {work_time * rate + bonus}")
