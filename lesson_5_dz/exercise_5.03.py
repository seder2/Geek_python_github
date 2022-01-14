# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

firm = {'Ivanov': 17332.12, 'Petrov': 34745.33, 'Sidorov': 12325.23, 'Naumov': 54640.12, 'Andreev': 12234.54,
        'Simanov': 13765.12, 'Evseev': 76210.12, 'Pavlov': 14000.55, 'Romanov': 18555.32, 'Balashov': 12345.21
        }
try:
    file_obj = open('staff_salary', 'w')
    for sur_name, salary in firm.items():
        file_obj.write(sur_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("staff_salary", "r") as f_obj:
    for line in f_obj:
        tokens = line.split(':')
        if float(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += float(tokens[1])
        count += 1
result = summa / count
print(f"сотрудники с окладом менее 20 тыс: {persons}")
print(f"средняя величина дохода сотрудников: {round(result, 2)}")
