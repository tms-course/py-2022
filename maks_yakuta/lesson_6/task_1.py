"""
1. Декодировать в строку байтовое значение, а затем результат преобразовать в байтовый
вид в кодировке 'Latin1' и затем снова декодировать в строку (результаты
всех преобразований выводить на экран).
b'r\xc3\xa9sum\xc3\xa9'
"""
binary_str = b'r\xc3\xa9sum\xc3\xa9'
decode_str = binary_str.decode()
print(decode_str)
encode_str = decode_str.encode('Latin1')
print (encode_str)
decode_str = encode_str.decode('Latin1')
print (decode_str)
