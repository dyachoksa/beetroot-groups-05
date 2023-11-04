import functools
import math
import time


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


def debug(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"Executing function {func.__name__!r} with {args=} and {kwargs=}")

        result = func(*args, **kwargs)

        print(f"Return value: {result}")

        return result
    
    return inner


@time_it
@debug
def calculate_pi(delay):
    print("Calculating PI...")

    # simulate calculation delay
    time.sleep(delay)

    print("PI:", math.pi)
    print("Done")

    return math.pi


# time_it_calculate_pi = time_it(calculate_pi)
# calculate_pi = time_it(calculate_pi)
# calculate_pi = time_it(debug(calculate_pi))

# time_it_calculate_pi()
pi = calculate_pi(0.1)


@time_it
def heavy_calculation(base = 10):
    result = 0
    for _ in range(base):
        result += math.pi * math.cos(base) - math.sin(base * 1_000_000) + math.sqrt(base * 1_000_000)

    return result

print(heavy_calculation(100_000))
