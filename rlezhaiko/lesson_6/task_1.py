"""
1. Декодировать в строку байтовое значение, а затем результат преобразовать в байтовый
вид в кодировке 'Latin1' и затем снова декодировать в строку (результаты
всех преобразований выводить на экран).
b'r\xc3\xa9sum\xc3\xa9'
"""

binary_string = b'r\xc3\xa9sum\xc3\xa9'
decoded_string = binary_string.decode()
print(decoded_string)
encoded_string_Latin1 = decoded_string.encode('Latin1')
print(encoded_string_Latin1)
decoded_string = encoded_string_Latin1.decode('Latin1')
print(decoded_string)




# résumé
# b'r\xe9sum\xe9'
#