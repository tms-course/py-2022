"""
Декодировать в строку байтовое значение, затем результат преобразовать в байтовый вид в кодировке Latin1
и затем результат снова декодировать в строку.
"""
byte_value = b'r\xc3\xa9sum\xc3\xa9'
str_decoded = byte_value.decode()
print(str_decoded)  #résumé

latin1_byte_value = str_decoded.encode('Latin1')
print(latin1_byte_value)  #b'r\xe9sum\xe9'

latin1_str_decoded = latin1_byte_value.decode('Latin1')
print(latin1_str_decoded)  #résumé
