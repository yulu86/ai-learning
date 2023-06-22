def sayNumber(number):
    result = ""
    if isDividedBy3(number):
        result += "Fizz"
    if isDividedBy5(number):
        result += "Buzz"
    if len(result) > 0:
        return result
    return f"{number}"


def isDividedBy3(number):
    return number % 3 == 0


def isDividedBy5(number):
    return number % 5 == 0


print(sayNumber(3))
print(sayNumber(5))
print(sayNumber(15))
print(sayNumber(1))
