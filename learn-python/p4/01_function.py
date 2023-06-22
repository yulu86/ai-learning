def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Yulu", "Xu")


def get_greeting(name):
    return f"Hi, {name}"


message = get_greeting("John")
print(message)


def increment(number, by=1):
    return number + by


result = increment(2)
print(result)
result = increment(2, by=3)
print(result)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user["id"])
    print(user["name"])


save_user(id=1, name="John", age=22)
