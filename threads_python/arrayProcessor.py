import threading
import time
import random


def add_array(identifier):
    print(f"Process Started for {identifier}")
    time.sleep(random.randint(1, 5))
    print(f"Process Ended for: {identifier}")


if __name__ == "__main__":
    sum_arry = [1, 2, 3]
    threads = []
    identifiers = ['first', 'second', 'third']
    for i in identifiers:
        threading.Thread(target=add_array(i)).start()
    print(f"Main Ended:")
