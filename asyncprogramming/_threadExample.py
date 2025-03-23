# _thread example which is a lower level module compared to threading module.
# We should consider using the more advanced thread module instead of low level thread option.
import threading
import time


def print_numbers(num):
    for i in range(5):
        print(f"{num}: {i}")
        time.sleep(0.5)


def print_letters(name):
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(f"{name} : {letter}")
        time.sleep(0.5)


if __name__ == "__main__":

    # create thread objects
    number_thread = threading.Thread(target=print_numbers, args=("Numbers",))
    letter_thread = threading.Thread(target=print_letters, args=("Letters",))

    # start the threads
    number_thread.start()
    print(f"No of active threads: {threading.active_count()}")
    letter_thread.start()
    print(f"No of active threads: {threading.active_count()}")
    # wait for both threads to finish
    number_thread.join()
    letter_thread.join()
    print(f"No of active threads: {threading.active_count()}")
    print("Printing from main:")
    print("both threasds have finished")
    print(threading.current_thread.__name__)
