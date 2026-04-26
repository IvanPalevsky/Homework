def swen(string: str) -> tuple:
    start = [0, 0]
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
    return tuple(start)
string = input()
print(swen(string))

