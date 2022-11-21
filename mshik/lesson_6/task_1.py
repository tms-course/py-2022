"""
Задание 1.

Декодировать в строку байтовые значения, а затем результат преобразовать в байтовый
вид в кодировке `Latin1` и затем результат снова декодироват в строку 
(результаты всех преобразований выводить на экран)
"""
decoded_string_utf8 = b"r\xc3\xa9sum\xc3\xa9".decode()
print(decoded_string_utf8) # résumé
encode_string_into_latin1 = decoded_string_utf8.encode("Latin1")
print(encode_string_into_latin1) # b'r\xe9sum\xe9'
decoded_string_latin1 = encode_string_into_latin1.decode("Latin1")
print(decoded_string_latin1) # résumé