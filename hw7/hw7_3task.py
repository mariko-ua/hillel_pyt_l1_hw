# Є 2 списки:
# [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
# [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
# Порахувати скільки разів числа з одного списку зустрічаються у ішому списку. Вивести у вигляді відформатованої таблиці.
#Upd:
# тут знайдено скільки елементів одного списку є у іншому списку
# додайте теж саме тільки навпаки
# скільки алементів другого списку входять також до першо списку

first_list = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
second_list = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
first_list.sort()
second_list.sort()
print(first_list)
print(second_list)

a = 0

print("Співпадіння елементів з першого списку у другому:")
print("{:<15} {:<15}".format("Ідекс елементу", "Елемент"))
for common_f in first_list:
    if common_f in second_list:
        print("{:<15} {:<15}".format(first_list.index(common_f), common_f)) # тут є проблема з індексом двійки. не розумію як вирішити проблему
        a += 1
print("Всього: ", a)

b = 0
print("Співпадіння елементів з другого списку у першому:")
print("{:<15} {:<15}".format("Ідекс елементу", "Елемент"))
for common_s in second_list:
    if common_s in first_list:
        print("{:<15} {:<15}".format(second_list.index(common_s), common_s))
        b += 1
print("Всього: ", b)


