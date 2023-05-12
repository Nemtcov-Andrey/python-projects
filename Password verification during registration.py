# Проверка пароля при регистрации. 
# Программа проверяет пароль, который должен состоять минимум из восьми символов, в нём должны быть хотя бы одна большая буква и хотя бы три цифры. 

while True: # бесконечный цикл
  password = list(input('Придумайте пароль: '))

    lengh = len(password) # кол-во символов в пароле

  capital_letters = sum(map(str.isupper, password)) # кол-во заглавных букв в пароле
  
  num_digit = sum(map(str.isdigit, password)) # кол-во цифр в пароле
  
  if lengh >= 8 and capital_letters >= 1 and num_digit >= 3:
    print('Это надежный пароль!')
    break
  else:
    print('Пароль ненадежный. Попробуйте еще раз')
