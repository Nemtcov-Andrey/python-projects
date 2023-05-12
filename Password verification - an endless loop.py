# Проверка пароля - бесконечный цикл.

password = int(input('Введите пароль: '))
while password != 235:
  print('Неверный пароль!')
  password = int(input('Попробуйте еще раз: '))
  print('Пароль верный!')
