# Завдання 2 (опціонально +5 до роботи)
#
# Створіть словник із випадковими числовими значеннями довжиною в 20 елементів.
# Необхідно їх (числові значення) перемножити і вивести на екран згенерований
# на початку словник та результат множення чисел.

import random


dictionary = {}
for i in range(20):
    key = f'Елемент {i+1}'
    value = random.randint(1, 100)
    dictionary[key] = value

print("Згенерований словник:")
for key, value in dictionary.items():
    print(f'{key}: {value}')


result = 1
for value in dictionary.values():
    result *= value

print("\nРезультат множення чисел:", result)