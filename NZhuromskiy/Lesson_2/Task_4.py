text_input = input("Введите любой текст: ").strip()
even_chars = text_input[::2]
odd_chars = text_input[1::2]
print(f"Введена строка \"{text_input}\"", end="".rjust(2))
print(even_chars, odd_chars, sep="".rjust(5), end="\n!!!\n")
