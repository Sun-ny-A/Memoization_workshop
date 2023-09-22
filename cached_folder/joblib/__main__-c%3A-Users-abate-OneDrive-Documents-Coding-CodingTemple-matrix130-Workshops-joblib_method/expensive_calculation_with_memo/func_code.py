# first line: 13
@memory.cache
def expensive_calculation_with_memo(x):
    result = 0
    for _ in range(10**6):
        result += x*x
    return result
