'''
a = int(input('Введите возраст: '))
if a < 16:
    print('В кинотеатр пускают с 16 лет')
else:
    print('Вход разрешен')
'''

'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    print(b)
else:
    print(a)
'''

'''
a = int(input('Введите число от 0 до 100: '))
if a >= 90:
    print("Отлично")
elif a >= 70:
    print("Хорошо")
elif a >= 50:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")
'''

'''
a = input('')
b = len(a)
if b > 10:
    print('Больше 10')
'''

'''
a = input('')
print(a[0], a[-1])
'''

a = input('Введите строку: ')
b = input('Введите слово: ')
if b in a:
    print('Есть')
else:
    print('Нету')