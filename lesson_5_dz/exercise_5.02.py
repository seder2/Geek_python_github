# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

my_list = {'John and Kate\n', 'Artur and Linda and Tony\n', 'Phil and Maria\n'}
with open('count.txt', 'w+') as f_obj:
    f_obj.writelines(my_list)
with open('count.txt') as f_obj:
    string = 0
    word = 0
    line: str
    for line in f_obj:
        string += line.count('\n')
        word = len(line.split())
        print(f'{word} слов/а в строке')
    print(f'Количества строк {string}')
