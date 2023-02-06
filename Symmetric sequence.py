# Симметричная последовательность.
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево, например:
# 1 2 3 4 5 4 3 2 1
# 1 2 1 2 2 1 2 1
# Программа определяет, какое минимальное количество и каких чисел из введенной пользователем последовательности надо приписать в конец этой последовательности, чтобы она стала симметричной.

def change(list1, list2):  # Переворачиваем первый список во второй
    for i in range(1, len(list1) + 1):
        list2.append(list1[- i])
    return list1, list2
    print('list1', list1)
    print('list2', list2)

def change_two(list_orig):  # Далее переворачиваем этот список
    i_list = []
    for i in range(1, len(list_orig) + 1):
        i_list.append(list_orig[- i])
    return i_list

nums = int(input('Кол-во чисел: '))
number_list = []
new_list = []

for _ in range(nums):
    num = int(input('Число: '))
    number_list.append(num)
print('\nПоследовательность:', number_list)

necessary_list = []
while True:
    if new_list == number_list:
        break
    else:
        new_list.clear()
        necessary_list.append(number_list[0])  # Создаем сами числа для симметрии
        number_list.remove(number_list[0])
        number_list, new_list = change(number_list, new_list)
necessary_list = change_two(necessary_list)

len_num = len(necessary_list)

print('Нужно приписать чисел:', len_num)
print('Сами числа:', necessary_list)