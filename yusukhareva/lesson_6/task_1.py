"""
Декодирует в строку байтовое значение, полученное значение преобазовывает 
в байтовый вид в кодировке 'Latin1', а затем снова декодирует в строку
"""
byte_orig = b'r\xc3\xa9sum\xc3\xa9'
str_orig = byte_orig.decode()
print("Оригинальная строка:", str_orig)
byte_decode = str_orig.encode("Latin1")
print ("Byte line: ", byte_decode)
str_changed = byte_decode.decode("Latin1")
print("Changed line: ", str_changed)