"""
task 1:
Декодировать в строку байтовое значение, а затем результат преобразовать в байтовый
вид в кодировке 'Latin1' и затем снова декодировать в строку (результаты
всех преобразований выводить на экран).
"""

byte_code = b'r\xc3\xa9sum\xc3\xa9'
string = byte_code.decode()
print(string)
latin1_code = string.encode(encoding='Latin1')
print(latin1_code)
string = latin1_code.decode('Latin1')
print(string)