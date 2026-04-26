# n = int(input('Введите целое число: '))
# for i in range(n, 0, -1):
#     print(i)
# print('Пуск!')
from itertools import repeat

# songs = ['песня1', 'песня2', 'песня3']
# for i in range(3):
#     for song in songs:
#         print(song)

# num = 7
# attempts = 0
# while True:
#     us_num = int(input('Угадайте число: '))
#     attempts += 1
#     if us_num == num:
#         print(f'Вы угадали за {attempts} попыток')
#         break

# while True:
#     temp = int(input('Ввеите температуру: '))
#     if temp == 0:
#         break
#     if temp >= 30:
#         print('Жарко')
#     elif temp <= 10:
#         print('Холодно')

n = int(input('Введите число: '))
for i in range(1, n+1):
    print('#'*i)