# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

number = int(input("Введите цифру: "))
list_1 = [7, 5, 3, 3, 2]
n = list_1.count(number)
for element in list_1:
    if n > 0:
        o = list_1.index(number)
        list_1.insert(o+n, number)
        break
    else:
        if number > element:
            m = list_1.index(element)
            list_1.insert(m, number)
            break
        elif number < list_1[len(list_1) - 1]:
            list_1.append(number)
print(list_1)