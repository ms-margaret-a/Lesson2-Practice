# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

string_1 = input("начните ввод: ")
n = string_1.split(' ')
for i, el in enumerate(n, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")