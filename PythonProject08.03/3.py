def char_frequency(text):
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency('hello world'))

