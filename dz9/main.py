# def game(player1, player2):
#     win_dict = {'rock': ['scissors'], 'paper': ['rock'], 'scissors': ['paper']}
#     if player1 == player2:
#         return 'ничья'
#     if player2 in win_dict[player1]:
#         return player1
#     else:
#         return player2
# print(game('rock', 'paper'))

# def date_converter(date: str) -> str:
#     date = date.split('.')
#     new_date = f'{date[2]}-{date[1]}-{date[0]}'
#     return new_date
# date = '12.12.2025'
# print(date_converter(date))

# def main(n):
#     a, b = 1, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# print([main(i) for i in range(7)])

def taxi_time(km=3, min_price=6, km_price=0.9):
    if km > 3:
        path_price = km_price * km - km_price * 3 + min_price
        return path_price
    return min_price
print('Поездка стоит:', taxi_time(), 'рублей')

# def is_prime():
#     while True:
#         n = input()
#         if n.lower() == 'exit':
#             exit()
#         int_n = int(n)
#         for i in range(2, int(int_n ** 0.5) + 1):
#             if int_n % i == 0:
#                 print('не простое')
#                 break
#         else:
#             print('простое')
# is_prime()