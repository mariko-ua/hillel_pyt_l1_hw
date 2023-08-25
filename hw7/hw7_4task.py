# Вводиться список цілих чисел. Всі числа списку знаходяться на одному рядку.
# У списку всі елементи різні. Поміняйте місцями мінімальний і максимальний елементи цього списку.
# Вхідні дані:
# 5 6 8 1 4 9 12
# Вихідні дані:
# 5 6 8 12 4 9 1
first_list = [8, 6, 5, 1, 4, 9, 12]
print(first_list)
max_index = first_list.index(max(first_list))
min_index = first_list.index(min(first_list))

first_list[min_index], first_list[max_index] = first_list[max_index], first_list[min_index]
print(first_list)