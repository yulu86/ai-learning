try:
    # with使用后自动关闭资源, 自动调用file的__exit__方法
    with open("04_with_statement.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues")
