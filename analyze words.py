# Анализ слова.
# Программа, которая считает количество уникальных букв в слове (это буквы, которые встречаются всего один раз).

word = input('Введите слово: ')
word_list = word
unique_letters = 0

for i in word_list:
    same_letters = 0
    for j in word_list:
        if j == i:
            same_letters += 1
    if same_letters  == 1:
        unique_letters += 1
print('Кол-во уникальных букв:', unique_letters)
