import threading
import time


def execute_thread():
    print(f"Starting the execution of the thread")
    currentThread = threading.current_thread()
    print(f" Current Thread: {currentThread.name}")
    time.sleep(5)
    print("Execution completed")


if __name__ == "__main__":

    threads = []
    for n in range(3):
        t = threading.Thread(target=execute_thread)
        threads.append(t)
        t.start()

    # joining the thread:
    for t in threads:
        t.join()

    print("Main Thread Ended")
