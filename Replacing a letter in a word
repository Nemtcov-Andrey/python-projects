# Программа заменяет букву в слове.

word = input('Введите слово: ')
replace_num = int(input('Номер буквы для замены: '))
replace_sym = input('Какой буквой заменяем? ')

sym_list = []  # создадим пустой список
for sym in word:  # пройдемся списком по слову
    sym_list.append(sym)  # добавим символ в список sym_list
sym_list[replace_num - 1] = replace_sym  # буква для замены = номер буквы - 1 по индексу

print('Измененное слово:')
for i in sym_list:  # пройдемся циклом по новому слову и выведем его
    print(i, end= '')
