# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator


def divide_by_null(divider, denominator):
    try:
        return divider / denominator
    except:
        return f"Результат равен 0"


div = DivisionByNull(10, 100)
print(divide_by_null(10, 0))
print(divide_by_null(10, 0.1))
print(divide_by_null(100, 0))
