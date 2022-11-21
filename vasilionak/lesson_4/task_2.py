number = int(input())
def factorial_recursive(number):
    if number == 1:
        return number
    else:
        return number*factorial_recursive(number-1)

print(factorial_recursive(number))

