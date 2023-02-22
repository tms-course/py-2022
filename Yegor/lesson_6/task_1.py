"""
1. Декодировать в строку байтовое значение, а затем результат преобразовать в байтовый
вид в кодировке 'Latin1' и затем снова декодировать в строку (результаты
всех преобразований выводить на экран).
b'r\xc3\xa9sum\xc3\xa9'
"""
byte_code = b'r\xc3\xa9sum\xc3\xa9'.decode()
print(byte_code)
byte_view = byte_code.encode('Latin1')
print(byte_view)
string = byte_view.decode('Latin1')
print(string)