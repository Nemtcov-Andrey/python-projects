# Поиск абсолютного пути файла.
# Программа принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

import os

def find_file(cur_path, file_name):
    print('переходим в ', cur_path)
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('    смотрим в ', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result

file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Folder')), 'Test.py') # Test.py - файл для поиска, Folder - папка где находится файл для поиска
if file_path:
    print('Абсолютный путь к файлу:', file_path)
else:
   print('Файл не найден')
