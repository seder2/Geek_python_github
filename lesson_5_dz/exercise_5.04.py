# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
from typing import List

my_lst = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("eng_rus.txt", 'r', encoding="utf-8")
    for line in file_obj:
        tokens = line.split(" - ")
        if tokens[0] in my_lst:
            word = my_lst[tokens[0]]
            result.append(word + ' - ' + tokens[1])
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("eng_rus_new.txt", "w", encoding="utf-8")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()

