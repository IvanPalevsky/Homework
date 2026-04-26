a = "hello world hi"
def longest(text):
    if not text:
        return None

    return max(text, key=len)


print(longest(a))

split()
