# def count_vowels(text):
#     vowels = 'aeiou'
#     count = 0
#     for i in text:
#         if i in vowels.lower():
#             count +=1
#     return count
# print(count_vowels('hello world'))



# int_list = [1, 2, 3, 11, 12, 13, 14, 15]
# new_list = filter(lambda i: i%2== 0 and i > 10, int_list)
# print(list(new_list))

def char_frequency(text):
    dict = {}
    for i in text.lower().replace(" ", ""):    #ДОДЕЛАТЬ
        dict[i] = text.lower().count(i)
    return dict
print(char_frequency('hello'))

# def is_palindrome(text):
#     new_text = text.lower().replace(" ", "")
#     if new_text == new_text[::-1]:
#         return True
#     return False
# print(is_palindrome('а роза упала на лапу Азора'))

# listt = ['hello', 'my name is Ivan']
# new_list = map(lambda i: i.upper().strip(), listt)
# print(list(new_list))

# def longest_word(text):
#     words = text.split()
#     return max(words, key=len)
# print(longest_word('hello world hi'))

# def group_by_length(words: list):
#     dict = {}
#     for i in words:
#         length = len(i)
#         if length not in dict:
#             dict[length] = []
#         dict[length].append(i)
#     return dict
# print(group_by_length(['hello', 'world', 'hi']))

# list = ['hello', 'world', 'hi']
# new_list = sorted(list, key=lambda i: i[-1])
# print(new_list)

# def count_long_words(text, n):
#     new_text = text.split()
#     return len(list(filter(lambda i: len(i) > n, new_text)))
# print(count_long_words('hello world', 3))