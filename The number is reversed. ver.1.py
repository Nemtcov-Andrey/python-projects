# Число наоборот. ver.1.

n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:
    digit = n1 % 10  # находим остаток - последнюю цифру
    n1 = n1 // 10  # делим нацело - удаляем последнюю цифру
    n2 = n2 * 10  # увеличиваем разрядность второго числа
    n2 = n2 + digit  # добавляем очередную цифру

print('Число наоборот:', n2)
