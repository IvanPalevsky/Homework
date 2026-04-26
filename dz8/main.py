# def kv(x):
#     total = 0
#     while x > 0:
#         digit = x % 10
#         total += digit ** 2
#         x //= 10
#     return total
# x = int(input())
# print(kv(x))

# numbers = [5, 8, 6, 3, 4]
# def sort_numbers(numbers: list) -> list:
#     result = []
#     for num in numbers:
#         if num % 2 != 0:
#             result.append(num)
#         else:
#             result.append(num // 2)
#     return result
# print(sort_numbers(numbers))
# не выполнено

# def operation_range(start, end, step, operator):
#     if operator == '+':
#         return sum(range(start, end+1, step))
#     elif operator == '-':
#         return sum(range(start, end+1, -step))
#     return None
#
#
# print(operation_range(1, 5, 1, '+'))

def new_list(list1, list2):
    return list1 + list2
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(new_list(l1, l2))