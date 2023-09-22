from joblib import Memory

memory = Memory("cached_folder", verbose=0) #verbose spits out all the output verbose=0 will not show you output

#NO MEMO
def expensive_calculation_no_memo(x):
    result = 0
    for _ in range(10**6):
        result += x*x
    return result

#MEMO with Joblib
@memory.cache
def expensive_calculation_with_memo(x):
    result = 0
    for _ in range(10**6):
        result += x*x
    return result

import timeit

time_no_memo = timeit.timeit("expensive_calculation_no_memo(30)", globals=globals(), number=100)
print(f"Time taken for expensive_calculation_no_memo: {time_no_memo}")

time_with_memo = timeit.timeit("expensive_calculation_with_memo(30)", globals=globals(), number=100)
print(f"Time taken for expensive_calculation_with_memo: {time_with_memo}")