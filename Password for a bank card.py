# Пароль на банковскую карту.

attemptsCount = 3 # кол-во попыток
for attempt in range (1, 4): # пройдемся циклом по попыткам
  pincode = int(input('Введите пин-код: '))
  if pincode == 1234:
    print('Пин-код верный! Держите ваши деньги!')
    break
  attemptsCount -= 1
  print('Пин-код неверный! Осталось попыток:', 3 - attempt)
if attemptsCount == 0:
  print('Ваша карта заблокирована. До свидания')
