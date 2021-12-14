# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

introduced_seconds = int(input("Введите пожалуйста время в секундах :"))
hours = introduced_seconds // 3600
minutes = (introduced_seconds - hours * 3600) // 60
seconds = (introduced_seconds - hours * 3600) % 60
print(f"{hours}:{minutes}:{seconds}")
