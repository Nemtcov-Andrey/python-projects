# Календарь.
# Программа принимает от пользователя день недели в виде строки и выводит его номер на экран.

day = input('Введите день недели: ').lower()
count = 0
for symbol in 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье':
  count +=1
  if symbol == day:
    print('Номер дня недели:', count)