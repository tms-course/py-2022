X0 = (17 / 2 * 3 + 2, 
     (17 / 2) * 3 + 2,
     (17 / 2 * 3) + 2)
X1 = (2 + 17 / 2 * 3, 
      2 + (17 / 2) * 3,
      2 + (17 / 2 * 3))
X2 = (19 % 4 + 15 / 2 * 3, 
      19 % 4 + (15 / 2) * 3, 
      (19 % 4) + (15 / 2 * 3)) 
X3 = ((15 + 6) - 10 * 4, 
      (15 + 6) - (10 * 4))
X4 = (17 / 2 % 2 * 3 ** 3, 
      (17 / 2) % 2 * 3 ** 3,
      (17 / 2 % 2) * 3 ** 3)

a = 20
b = 2


def is_valid_parenthes(expressions):
    if not expressions:
        return False
    is_identical = expressions.count(expressions[0]) == len(expressions)
    print(f"Expressions are identical: {is_identical}")
    return is_identical


def calculate_formula(x, y):
    return (abs(x) - abs(y)) / (1 + abs(x * y))


# Task 1
print(f"Sum: {a + b}")
print(f"Subdivision: {a - b}")
print(f"Multiply: {a * b}")
print(f"Pow: {a ** b}")
print(f"Division by modulo: {a % b}")
print(f"Division: {a //  b}")


# Task 2
is_valid_parenthes(X0)
is_valid_parenthes(X1)
is_valid_parenthes(X2)
is_valid_parenthes(X3)
is_valid_parenthes(X4)


# Task 3
print(f"Calculate formula: {calculate_formula(a, b)}")
