"""
1. Декодировать в строку байтовые значения, а затем результат преобразовать в байтовый
вид в кодировке `Latin1` и затем результат снова декодировать в строку
(результаты всех преобразований выводить на экран)
"""

decoding_string = b"r\xc3\xa9sum\xc3\xa9".decode()
print(decoding_string)

conversion_string = decoding_string.encode("Latin1")
print(conversion_string)

decoding_string = conversion_string.decode("Latin1")
print(decoding_string)
