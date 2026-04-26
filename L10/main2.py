def swen(string: str, x: int, y: int) -> tuple:
    start = [x, y]
    low_str = string.lower()
    if 's' in low_str:
        len_s = low_str.count('s')
        start[1] -= len_s
    elif 'n' in low_str:
        len_n = low_str.count('n')
        start[1] += len_n
    elif 'w' in low_str:
        len_w = low_str.count('w')
        start[0] -= len_w
    elif 'e' in low_str:
        len_e = low_str.count('e')
        start[0] += len_e
    print(tuple(start))
while True:
    try:
        str = input('Введите строку: ')
        x = int(input('Введите х: '))
        y = int(input('Введите у: '))
        swen(str, x, y)
        break
    except ValueError:
        print('Вводите правильные типы данных')