import threading
import time
from rich.console import Console

console = Console()


class localThread(threading.Thread):

    def __init__(self, name, callable):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = 1
        self.callable = callable

    def run(self):
        print(f"inside run: printing the counter: {self.counter} ")
        self.callable()


def mycustomTask():
    for i in range(0, 5):
        time.sleep(1)
        print(f"Custom Task Counter: {i}")


if __name__ == "__main__":
    t1 = localThread(name="counter Thread", callable=mycustomTask)
    t1.start()
    t1.join()
    console.print("Process Completed",  style="yellow")
