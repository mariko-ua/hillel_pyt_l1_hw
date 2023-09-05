# Завдання 5
#
# Створіть словник з рядка 'python is good language to code' наступним чином:
# як ключі візьміть літери рядка, а значеннями нехай будуть числа, що відповідають
# кількості входження даної літери в рядок.







# don`t send


list_one = 'python is good language to code'

my_dict = {}
for letter in list_one:
    if letter != ' ':
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1

print(my_dict)