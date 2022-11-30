"""Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'.Затем результат преобоазлвать в байтовый вид в кодировке 'Lathin'
 и затем результат снова деродировать в троку (результаты всех преобоазований выводить на экран)"""


data = b'r\xc3\xa9sum\xc3\xa9'
data_decode_utf = data.decode("utf-8")
print(data_decode_utf)
data_encode_latin = data_decode_utf.encode("Latin1")
print(data_encode_latin)
data_decode_latin = data_encode_latin.decode("Latin1")
print(data_decode_latin)
