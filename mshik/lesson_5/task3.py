"""
Задание 3.

При помощи filter() из кортежа слов отфильтровать толко те,
которые являются полиндромами (которые читаются одинаково в обе стороны).
"""

polindroms = list(filter(lambda word: word == word[::-1], ["hello", "abba", "test", "anna"]))
print(f"Polindroms: {polindroms}")