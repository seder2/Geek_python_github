# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

my_list = input("Введите элементы списка: ").split()
print(my_list)

my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)


# number_list = list("123456789")
# print(number_list[1::2])
# print(number_list[::2])
# print(number_list[:-1:2])
# print(number_list)