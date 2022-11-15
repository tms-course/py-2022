"""
To implement lambda function that returns 'четное' if argument is even, otherwise 'нечетное'
"""
input_number = int(input())
output = (lambda x: 'четное' if x % 2 == 0 else 'нечетное')(input_number)
print(output)
