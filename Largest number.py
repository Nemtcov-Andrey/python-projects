# Наибольшее число среди всех.
# Программа находит наибольшее число среди всех.

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
        hight_num = number
print('Наибольшее число среди всех:', hight_num)
