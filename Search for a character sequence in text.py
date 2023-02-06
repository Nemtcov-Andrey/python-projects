# Поиск последовательности символа в тексте.
# Программа получает на вход строку, подсчитывает в ней самую длинную последовательность нужного символа и выводит ответ на экран.

text = input('Введите строку:  ')
symbol = input('Введите букву для поиска: ')
count_s = 0
count_max = 0

for symbol in text:
  if symbol == 'symbol':
    count_s += 1
    if count_s > count_max:
      count_max = count_s
  else:
    count_s = 0
print('Самая длинная последовательность: ', count_max)
