def calculate_xfactor(age):
    if age <= 0:
        # 抛出异常
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(ex)
