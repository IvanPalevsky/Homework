def count_long_words(text, n):
    words = text.split()

    long_words = list(filter(lambda w: len(w) > n, words))
    return len(long_words)
print(count_long_words("abcdsdffd", 3))

