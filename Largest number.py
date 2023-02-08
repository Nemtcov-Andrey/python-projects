# Наибольшее число.
# Программа находит наибольшее число среди всех и его сумму цифр.

seqNum = int(input('Сколько чисел будет? '))
max_num = 0
for num in range(1, seqNum + 1):
  print('Введите', num, '-e число: ')
  number = int(input())
  temp = number
  summ = 0
  while temp > 0:
    summ += temp % 10
    temp //= 10
  if summ > max_num:
    max_num = summ
    hight_num = number
print('Наибольшее число среди всех', hight_num, 'и его сумма цифр =', max_num)
