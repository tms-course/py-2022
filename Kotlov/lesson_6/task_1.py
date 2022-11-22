bytes_utf_8 = b'r\xc3\xa9sum\xc3\xa9'

str_utf_8 = bytes_utf_8.decode()
print(f'Decode utf-8: {str_utf_8}')

bytes_latin_1 = str_utf_8.encode('Latin1')
print(f'Encode Latin1: {bytes_latin_1}')

str_latin_1 = bytes_latin_1.decode('Latin1')
print(f'Decode Latin1: {str_latin_1}')
