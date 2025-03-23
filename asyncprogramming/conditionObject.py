import threading
import time
import random


class ProducerConsumer:

    def __init__(self):
        self.condition = threading.Condition()
        self.buffer = []
        self.max_buffer_size = 5

    def produce(self, item):
        with self.condition:
            while len(self.buffer) == self.max_buffer_size:
                print(f"Producer waiting buffer full")
                self.condition.wait()

            self.buffer.append(item)
            print(f"Produced an item: {item}")
            self.condition.notify_all()

    def consume(self):
        with self.condition:
            while not self.buffer:
                print(f"Buffer is empty therefore waiting")
                self.condition.wait()

            item = self.buffer.pop(0)
            print(f"Consumed : {item}")
            self.condition.notify_all()
            return item


def producer(pc):
    for i in range(10):
        time.sleep(random.random())  # Simulate producing time
        pc.produce(i)


def consumer(pc):
    for _ in range(10):
        time.sleep(random.random())  # Simulate consuming time
        pc.consume()


if __name__ == "__main__":

    pc = ProducerConsumer()

    # consumer thread
    consumer_thread = threading.Thread(target=consumer, args=(pc,))
    # provider
    provider_thread = threading.Thread(target=producer, args=(pc,))
    provider_thread.start()
    consumer_thread.start()
    provider_thread.join()
    consumer_thread.join()
    print('Main Processing Completed:')
