from functools import lru_cache
import timeit

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"Finished in {end_time - start_time:.7f}s: {func.__name__}({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    user_input = int(input("Enter the value of n: "))
    fib(user_input)


