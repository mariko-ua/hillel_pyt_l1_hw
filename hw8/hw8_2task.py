# Напишіть програму, яка виводить квадратну матрицю
# розміру N на N заповнену випадковими числами.
# N = запросити у користувача
# Вивести значення у вигляді матриці чисел.
# Вивести в термінал - суму чисел по діагоналі
# Вивесті на екран суму чисел остнанього стовбця.
# ( Можна використити вираз і функцію sum() )

import random

n = int(input("Введіть число: "))
matrix = [
    [
        # f"{random.randint(-42, 42):3}"
        random.randint(-42, 42)
        for j in range(n)]
    for i in range(n)
]

for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

print("_" * 30)

diagonal_sum = sum(matrix[diagonal][diagonal] for diagonal in range(n))
print("Сума чисел по діагоналі: ", diagonal_sum)

last_column = sum(
    matrix[column][-1]
    for column in range(n)
)
print("Сума чисел в останьому стовпці: ", last_column)

