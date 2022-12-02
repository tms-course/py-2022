words = ("оно", "иди", "иду", "летел", "кабак", "бегу")
words_palindrome = list(filter(lambda x: x == x[::-1], words))
print(words_palindrome)