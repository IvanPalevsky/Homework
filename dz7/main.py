# name = input('Введите имя: ')
# def hello(name: str):
#     print('Привет, ', name)
# hello(name)

# def kv(num):
#     return num*num
# print(kv(10))

# def num(number):
#     return number % 2 == 0
# print(num(6))

# def summ(num1, num2):
#     return num1 + num2
# print(summ(1, 2))

# def lenght(string):
#     return len(string)
# print(lenght("hello world"))

# def max(num1, num2):
#     if num1 > num2:
#         return num1
#     return num2
# print(max(2, 2))

# def lenght(word):
#     return len(word) > 5
# print(lenght('hellooo'))

# def repeat(string, n):
#     return string * n
# print(repeat("Hello World", 3))

# def upper(string):
#     return string.upper()
# print(upper("Hello World"))

def calculator(a, b, string):
    if string == '+':
        return a + b
    elif string == '-':
        return a - b
print(calculator(1, 2, '+'))