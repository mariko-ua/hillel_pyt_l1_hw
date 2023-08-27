# Створити список чисел в діапазоні 10, 250, необхідно видалити всі входження чисел, які
#  діляться без остачі на 20, із нього. Вивести результуючий список в термінал.

number_list = list(range(10, 251))
new_list = []
for i in number_list:
    if i % 20 == 0:
        number_list.remove(i)
print(number_list)
