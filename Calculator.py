# Калькулятор.
# Программа запрашивает у пользователя число и действие, которое нужно с ним сделать: вывести сумму его цифр, максимальную или минимальную цифру.

def sum_num(n):
    summa = 0
    while n > 0:
        number = n % 10
        summa += number
        n = n // 10
    print('Сумма цифр =', summa)

def max_num(n):
    maximum = n % 10
    while n > 0:
        i = n % 10
        if i <= maximum:
            maximum = i
        n //= 10
    print('Максимальная цифра =', maximum)

def min_num(n):
    minimum = n % 10
    while n > 0:
        i = n % 10
    if i <= minimum:
        minimum = i
    n //= 10
    print('Минимальная цифра =', minimum)

n = int(input('Введите любое число: '))
print()
print('1 - Вывести сумму цифр')
print('2 - Вывести максимальную цифру')
print('3 - Вывести минимальную цифру')
action = int(input('\nКакое действие выполнить? Выберите цифру: '))
print()

if action == 1:
    sum_num(n)
elif action == 2:
    max_num(n)
elif action == 3:
    min_num(n)
else:
    print('Ошибка ввода!')

