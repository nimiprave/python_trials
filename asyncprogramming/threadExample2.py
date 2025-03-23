import threading
from rich.console import Console

console = Console()
# list of emlpoyees with their first name, last name and age
list_of_employees = [{"name": "John", "last_name": "Doe", "age": 30},
                     {"name": "Jane", "last_name": "Doe", "age": 25},
                     {"name": "Jack", "last_name": "Smith", "age": 40},
                     {"name": "Jill", "last_name": "Smith", "age": 35},
                     {"name": "James", "last_name": "Brown", "age": 50},
                     {"name": "Jenny", "last_name": "Brown", "age": 45}]

# go is to split the list of employess into two list and process them in paraller


def process_employees(employees, thread_name):
    console.print(
        f"Thread {thread_name} processing employees", style="magenta")
    for employee in employees:
        print(employee)


# main
if __name__ == "__main__":

    # breaking the list into two for process
    mid_size = int(abs(len(list_of_employees) / 2))
    print(mid_size)
    first_list = list_of_employees[:mid_size]
    second_list = list_of_employees[mid_size:]

    thread1 = threading.Thread(target=process_employees, args=(
        first_list, "first Thread",))
    thread2 = threading.Thread(target=process_employees, args=(
        second_list, "second thread",))

    # split the list into two for processing.
    thread1.start()
    thread2.start()

    # thread1.join()
    # thread2.join()
    console.print("Process Completed", style="bold yellow")
