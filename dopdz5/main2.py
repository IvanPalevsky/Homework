words = ['Apple', 'Banana']
substr = 'a'
def find_substring(string, substr):
    string = words.split().lower()
    for i in string:
        if i.startswith(substr):
            return i


print(find_substring(words, substr))