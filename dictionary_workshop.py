# Without Memoization
def factorial_no_memo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_no_memo(n-1)

# With Memoization using Dictionary
memo = {}
def factorial_with_memo(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial_with_memo(n-1)
    memo[n] = result
    return result

# We can seperate this logic into a decorator function
def memoize_factorial(func):
    memo = {}
    
    def wrapper(n):
        if n in memo:
            return memo[n]
        result = func(n)
        memo[n] = result
        return result
    
    return wrapper

@memoize_factorial
def wrapped_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * wrapped_factorial(n - 1)


import timeit

# Benchmark for factorial_no_memo
time_no_memo = timeit.timeit("factorial_no_memo(30)", globals=globals(), number=1000)
print(f"Time taken for factorial_no_memo: {time_no_memo}")

# Benchmark for factorial_with_memo
time_with_memo = timeit.timeit("factorial_with_memo(30)", globals=globals(), number=1000)
print(f"Time taken for factorial_with_memo: {time_with_memo}")

#with memoization there was much faster processing time.