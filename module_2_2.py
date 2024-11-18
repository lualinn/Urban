# Вводим три целых числа
first = int(input())
second = int(input())
third = int(input())

# Проверяем условия
if first == second == third:
    print(3)  # Все числа равны
elif first == second or first == third or second == third:
    print(2)  # Хотя бы два числа равны
else:
    print(0)  # Все числа разные