# Программа считает количество букв и цифр в тексте.

def count_letters(text, number, letter):
    a = 0
    b = 0
    for i in text:
        if i == number:
            a += 1
        elif i == letter:
            b += 1

    print('Количество цифр', number, ':', a)
    print('Количество букв', letter, ':', b)

text = input('Введите текст: ')
number = input('\nКакую цифру ищем? ')
letter = input('Какую букву ищем? ').lower()
print()
count_letters(text, number, letter)
