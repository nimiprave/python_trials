import threading
import time
import requests


def crawl(link, delay=3):
    print(f"crawl started at the {link}")
    time.sleep(delay)
    print(f"crawl ended for {link}")


links = ["https://python.org",
         "https://docs.python.org", "https://pep.python.org"]


if __name__ == "__main__":

    # current thread
    currentThread = threading.current_thread()
    print(f"Main Thread name{currentThread}")

    # Start the thread for each link
    threads = []
    for link in links:
        # using args to pass positional arguments and kwargs for keywork arguments
        t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
        print(f"Inside thread: {t.getName()}")
        threads.append(t)

    # inspecting the threading t

    # start each thread
    for t in threads:
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()
