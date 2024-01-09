import asyncio
import time
from random import randint


async def count(idx):
    sleep_time = randint(1, 3)
    # sleep_time = 2
    print(f"Start #{idx} ({sleep_time} seconds)...")
    await asyncio.sleep(sleep_time)
    print(f"End #{idx}")


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
