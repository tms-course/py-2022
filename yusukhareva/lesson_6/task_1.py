"""
Декодирует строку в байтовое значение, полученное значение в строку
:param byte_orig: байтовое значение оригинальной строки
:param str_orig: оригинальная строка
:param bite_decode: байтовое значение строки в кодировке 'Latin1'
:param str_changed: переведенная строка из байтового значения в кодировке 'Latin1'

"""
byte_orig = b'r\xc3\xa9sum\xc3\xa9'
str_orig = byte_orig.decode()
print("Оригинальная строка:", str_orig)
byte_decode = str_orig.encode("Latin1")
print ("Byte line: ", byte_decode)
str_changed = byte_decode.decode("Latin1")
print("Changed line: ", str_changed)
