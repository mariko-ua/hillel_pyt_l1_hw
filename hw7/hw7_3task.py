# Є 2 списки:
# [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
# [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
# Порахувати скільки разів числа з одного списку зустрічаються у ішому списку. Вивести у вигляді відформатованої таблиці.

first_list = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
second_list = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
first_list.sort()
second_list.sort()
print(first_list)
print(second_list)
third_list = []
a = 0
for common in first_list:
    if common in second_list:
        third_list.append(common)
        a += 1
third_list.sort()
print(third_list)

