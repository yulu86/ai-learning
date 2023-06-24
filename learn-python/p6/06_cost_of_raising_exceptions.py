from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        # 抛出异常
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

# 执行代码10000遍，记录耗时
timeCost1 = timeit(code1, number=10000)
print("Code1 time cost:", timeCost1)

timeCost2 = timeit(code2, number=10000)
print("Code2 time cost:", timeCost2)

# 结论：异常较为耗时，通常用简单的if判断解决，减少耗时
