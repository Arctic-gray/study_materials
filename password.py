#Генерация пароля, по умолчанию генерируется пароль из 8 символов

import random #подключение модуля

def passw_generator(count_char = 8):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z', '1', '2', '3', '4',
           '5', '6', '7', '8', '9', '0', '~',
           '@', '#', '$', '%', '&', '?', '*',
           '(', ')', '[', ']']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(arr)) #append() - добавление элемента в конец последовательности
    return ''.join(passw) #соединяет элементы в строку с разделителем, в данном случае разделитель - ''

#print(passw_generator())
#print(passw_generator(10))

count_c = int(input('Введите количество символов в пароле: '))
print(passw_generator(count_c))
