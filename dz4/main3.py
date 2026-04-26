'''
a = {'1': 1, '2': 2, '3': 3}
print(a)
a.update({'4': 4})
a.update({(1, 2): [3, 4]})
a.get('1')
a.pop('2')
print(a)
print(a.keys())
'''

'''
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)
'''

b = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
a = int(input('Введите число от 1 до 7: '))
if a in b.keys():
    print(b.get(a))
