def swen(string: str, x: int, y: int) -> tuple:
    start = [x, y]
    while x in range(0, 101) and y in range(0, 101):
        low_str = string.lower()
        if 's' in low_str:
            len_s = low_str.count('s')
            start[1] -= len_s
        if 'n' in low_str:
            len_n = low_str.count('n')
            start[1] += len_n
        if 'w' in low_str:
            len_w = low_str.count('w')
            start[0] -= len_w
        if 'e' in low_str:
            len_e = low_str.count('e')
            start[0] += len_e
        print(tuple(start))
        break
    else:
        print('Начальные координаты могут быть в диапазоне от 0 до 100')
        start = [0, 0]
        print(tuple(start))
    if not (0 <= start[0] <= 100 and 0 <= start[1] <= 100):
        print('Координаты вышли за пределы диапазона')
        return (x, y)
    return tuple(start)

while True:
    try:
        str = input('Введите строку: ')
        x = int(input('Введите х: '))
        y = int(input('Введите у: '))
        swen(str, x, y)
        break
    except Exception as e:
        print(e)