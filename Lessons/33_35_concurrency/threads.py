import concurrent.futures
import functools
import time
import threading


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


def download_image(url):
    print("Starting dowload of image {}".format(url))

    # actual http/xml/rpc requests
    time.sleep(2)

    print("Finished donload of image {}".format(url))


@time_it
def download_all_images(urls):
    # threads = []
    # for url in urls:
    #     t = threading.Thread(target=download_image, args=(url,))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_image, urls)


if __name__ == "__main__":
    urls = [
        "http://example.com/image.jpg",
        "https://unsplash.com/image_1234.jpg",
        "https://pixart.com/images/illustration.jpg",
        "https://unsplash.com/image_965.jpg",
        "https://unsplash.com/image_000.jpg",
    ]

    download_all_images(urls)
