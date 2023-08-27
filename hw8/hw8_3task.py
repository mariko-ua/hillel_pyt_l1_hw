# Напишіть програму, Яка генерує список із 15 випадкових чисел.
# Виведіть:
# Так - якщо сумма непарних чисел у списку більша за суму парних чисел
# Ні - у всіх інших випадках

import random
list_random = [
    random.randint(-100, 100)
    for i in range(4)
]
print(list_random)
for i in list_random:
    if sum(list_random, i % 2) > sum(list_random, i % 2 == 0):
        print("yes")
        break
    else:
        print("no")
        break
print("непарні: ", sum(list_random, i % 2))
print("парні: ", sum(list_random, i % 2 == 0))
