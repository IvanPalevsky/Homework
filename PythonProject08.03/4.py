def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("А роза упала на лапу Азора"))

