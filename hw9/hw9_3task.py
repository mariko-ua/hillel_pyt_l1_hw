# Завдання 3 (опціонально +5 до роботи )
#
# Створіть словник використовуючи генератор словника, у якому ключами
# будуть числа від 1 до 10, а значеннями ці числа, зведені в куб.


dictionary = {i: i**3 for i in range(1, 11)}
print(dictionary)