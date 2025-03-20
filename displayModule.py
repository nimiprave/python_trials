import time


def display_hello(greetings):
    print(greetings + " Hello!")


def display_goodbye(greetings):
    print(greetings + "Goodbye!")


def display_welcome(greetings):
    print(greetings + "Welcome!")


def wait():
    print("Waiting started")
    time.sleep(5)
    print("Waiting finished")
