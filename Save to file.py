# Сохранение в файл.
# Программа запрашивает у пользователя путь сохранения введенной им строки text. Затем в этот файл сохраняется значение переменной text. 
# Если этот файл уже существует, то спрашивается у пользователя о необходимости перезаписи этого файла.
# Обеспечивается контроль ввода: указанный из папок путь должен существовать на диске.

import os

def save(path, name):
    replace_sym = os.path.join(path)
    abs_path = os.path.abspath(replace_sym)
    return abs_path

text = input('Введите строку: ')
name_path = input('Куда хотите сохранить документ: ')
file_name = input('Введите имя файла: ')

abs_path = os.path.abspath(save(name_path, file_name))
print(abs_path)
check = os.path.exists(abs_path)
if check:
    question_checking = input('Вы действительно хотите перезаписать файл? ')
    if question_checking == 'да'.lower():  
        save_str = open(file_name, '.txt', 'w', encoding='utf-8')
        save_str.write(text)
        print('Файл успешно перезаписан!')
        save_str.close()
    else:
        print('Файл не записан')
else:
    save_str = open('my_document.txt.txt', 'w', encoding='utf-8')
    save_str.write(text)
    print('Файл успешно сохранен!')
    save_str.close()
