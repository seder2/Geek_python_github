# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_list = []
while True:
    data = input("Введите данные:")
    if data != '':
        newline: str = data + '\n'
        user_list.append(newline)
    else:
        print(user_list)
        exit()

    with open("test.txt", "w") as f_obj:
        f_obj.writelines(user_list)
