import threading
import time
import random
from rich.console import Console
from rich.table import Table
console = Console()

# Creating the table for display
table = Table()
table.add_column("ThreadName")
table.add_column("Description")


def add_array(identifier):
    print(f"Process Started for {identifier}")
    time.sleep(random.randint(1, 5))
    print(f"Process Ended for: {identifier}")


if __name__ == "__main__":
    sum_arry = [1, 2, 3]
    threads = []
    identifiers = ['first', 'second', 'third']
    for i in identifiers:
        # if args is not used
        threads.append(threading.Thread(target=add_array, args=(i,)))
        # threading.Thread(target=add_array(i)).start()

    for thread in threads:
        thread.start()

    print(f"Main Ended:")


# I don;t understand the behavior. The Threads are exectuted in the same order.
# and the main thread is exiting after all the threads are finished the processing.
