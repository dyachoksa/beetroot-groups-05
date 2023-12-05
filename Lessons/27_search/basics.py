import functools
import random
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


@time_it
def linear_search(items, value):
    for cur_indx, item in enumerate(items):
        if item == value:
            return cur_indx

    return -1


@time_it
def binary_search(items, value):
    first_idx = 0
    last_idx = len(items) - 1
    idx = -1

    while first_idx <= last_idx and idx == -1:
        middle_idx = (first_idx + last_idx) // 2

        if items[middle_idx] == value:
            idx = middle_idx
            break

        if items[middle_idx] < value:
            first_idx = middle_idx + 1
        else:
            last_idx = middle_idx - 1

    return idx


@time_it
def binary_search_with_sorted(items, value):
    items_sorted = sorted(items)

    first_idx = 0
    last_idx = len(items_sorted) - 1
    idx = -1

    while first_idx <= last_idx and idx == -1:
        middle_idx = (first_idx + last_idx) // 2

        if items_sorted[middle_idx] == value:
            idx = middle_idx
            break

        if items_sorted[middle_idx] < value:
            first_idx = middle_idx + 1
        else:
            last_idx = middle_idx - 1

    return idx


if __name__ == "__main__":
    n = 10_000_000

    value = 9_999

    numbers = [random.randint(1, 100_000_000) for _ in range(n)]
    numbers.append(value)

    numbers_sorted = sorted(numbers)

    idx = linear_search(numbers, value)
    print(f"{value} is inside 'numbers' under index {idx}")

    idx = binary_search(numbers_sorted, value)
    print(f"{value} is inside 'numbers' under index {idx}")

    idx = binary_search_with_sorted(numbers, value)
    print(f"{value} is inside 'numbers' under index {idx}")
