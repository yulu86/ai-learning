message = "Hello World"


def greet(name):
    message = "a"


def send_email(name):
    global message
    message = "b"


greet("John")
print(message)

send_email("Dog")
print(message)
