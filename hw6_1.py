# Користувач вводить окремо рядок (string) і наступним кроком водить один символ (char).
# Необхідно здійснити пошук у рядку `string` всіх символів `char`.
# Для вирішення потрібно використовувати тільки функцію `find()`(rfind()), оператори `if` і `for`(while)

str = input("Write your string: ")
char = input("Write your char: ")

for find in range(len(str)):
    if str[find] == char:
        print(f"Символ '{char}' знайдено. Номер індексу {find}")

