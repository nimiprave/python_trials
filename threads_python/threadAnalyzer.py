import threading
import time


def run():
    print(f"Starting the child threads:")
    time.sleep(5)
    print(f"Ending the child threads:")


if __name__ == "__main__":

    thread = threading.current_thread()
    print(f"Current Thread: {thread.name}")

    mainThread = threading.main_thread()
    print(f"Main Thread: {thread.name}")

    print(
        f" Active count of Threads in the Systembefore child threads: {threading.active_count()}")

    threads = []
    for n in range(5):
        t = threading.Thread(target=run)
        threads.append(t)

    print(
        f" Active count of Threads in the System before child threads started: {threading.active_count()}")

    # starting the threads.
    for t in threads:
        t.start()

    print(
        f" Active count of Threads in the System after child threads started: {threading.active_count()}")

    # joining the threads
    for t in threads:
        t.join()

    print(
        f" Active count of Threads in the System after child threads joined: {threading.active_count()}")
