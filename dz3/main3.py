'''
a = 'орпрп рорп ропор'
if a.count(' ') >= 2:
    print('Много слов')
'''

'''
a = 'парпапа опорп ааор'
a_list = a.split()
if len(a_list) > 2:
    print(a_list)
'''

'''
a = ['Паооол', 'ОАОНЕО', 'Влодвпо']
if all(i and i[0].isupper() for i in a):
    print('Корректно')
'''

'''
a = ['олфваыр', '2', '3', 'олфваыр']
if a[0] == a[-1]:
    print('Совпадает')
'''

a = input('')
a_list = a.split()
if len(a_list) == 2:
    print('Имя и фамилия')