'''
a = input('Введите что-нибудь: ')
if a.startswith('А'):
    print('Да')
else:
    print('Нет')
'''

'''
a = input('')
b = len(a)
if b > 10:
    print('Длинная')
else:
    print('Короткая')
'''

'''
a = input('')
b = a[:]
if 'python' in b:
    print('Найдено')
'''

'''
a = input('')
if a.endswith('!'):
    print('Восклицание')
'''

'''
a = input('')
if a.isdigit():
    print('Число')
'''

'''
a = input('')
if a == a.upper():
    print('Верхний')
'''

'''
a = input('')
if a == a.lower():
    print('Нижний')
'''

'''
a = input('')
if ' ' in a:
    print('Есть пробел')
'''

'''
a = input('')
b = len(a) - 1
if b / 2:
    print('Четная длина')
'''

'''
a = input('')
if a.startswith(a[0]) and a.endswith(a[0]):
    print('Совпадает')
'''

'''
a = input('')
b = a.count('а')
if b > 3:
    print('Много а')
'''

'''
a = input('')
if a.lower() == 'admin':
    print('Доступ разрешен')
'''

'''
a = input('')
if a[0].isalpha():
    print('Буква')
'''

'''
a = input('')
b = len(a)
if b < 1:
    print('Пустая')
'''


a = input('')
if '@' in a:
    print('Похоже на email')

