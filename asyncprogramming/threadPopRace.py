# program to demonstrate that multiple threads are working on the same resource
# in this case, the dictionary.

# import the thread
import threading
import time

# Create a custom thread by overing the run method of the Thread object


class Racer(threading.Thread):

    def __init__(self, runnable, args):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.args = args

    def run(self):
        self.runnable(self.args)


def picker(name_list):
    # print(f"I have been called in thread: {threading.current_thread().name}")
    nlist = (name_list[0])
    for i in nlist:
        print(f"{threading.current_thread().name} : {nlist.pop()}")
        time.sleep(1)


if __name__ == "__main__":

    # list of emlpoyees with their first name, last name and age
    list_of_employees = [
        {"name": "John", "last_name": "Doe", "age": 30},
        {"name": "Jane", "last_name": "Doe", "age": 25},
        {"name": "Jack", "last_name": "Smith", "age": 40},
        {"name": "Jill", "last_name": "Smith", "age": 35},
        {"name": "James", "last_name": "Brown", "age": 50},
        {"name": "Jenny", "last_name": "Brown", "age": 45}
    ]

    t1 = Racer(runnable=picker, args=(list_of_employees,))
    t2 = Racer(runnable=picker, args=(list_of_employees,))

    # start the threads
    t1.start()
    t2.start()

    # join the main thread
    t1.join()
    t2.join()
    print(f"Main Thread completed")
