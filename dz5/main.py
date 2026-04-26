# goods = {'Карандаш': 25, 'Стерка': 30, 'Ручка': 35}
# for name, number in goods.items():
#     print(f'Товар: {name}, кол-во: {number}')

# pupils = {'Артем': 8, 'Тимофей': 6, 'Дима': 3}
# for key, value in pupils.items():
#     if value >= 4:
#         print(key)

# word = input('Введите слово: ')
# letter_count = {}
# for i in word:
#     if i in letter_count:
#         letter_count[i] += 1
#     else:
#         letter_count[i] = 1
# print(letter_count)

# players = {'Игрок1': 100, 'Игрок2': 200, 'Игрок3': 350}
# max_player = ''
# max_score = int()
# for player, score in players.items():
#     if score > max_score:
#         max_score = score
#         max_player = player
# print(f'Игрок с максимумом: {max_player}')

schedule = {'Понедельник': ['дз', 'тренировка'], 'Вторник': ['уборка', 'прогулка']}
for day, tasks in schedule.items():
    print(f'{day}:')
    for task in tasks:
        print(f'- {task}')