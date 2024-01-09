import concurrent.futures
import functools
import time
import math
import os


def time_it(func):
    @functools.wraps(func)
    def inner(*argv, **kwarg):
        start_time = time.perf_counter()

        result = func(*argv, **kwarg)

        end_time = time.perf_counter()

        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.5f} secs")

        return result
    
    return inner


def do_math_calculation(idx):
    print(f"Processing #{idx}...")
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    v = 0
    for i in range(1_000_000):
        v += i*i + math.pow(i, 10) + math.sin(i) + math.cos(i)

    print(f"End processing #{idx}")


@time_it
def calculate_something(n_times):
    # for _ in range(n_times):
    #     do_math_calculation()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(do_math_calculation, list(range(n_times)))


if __name__ == "__main__":
    calculate_something(10)
