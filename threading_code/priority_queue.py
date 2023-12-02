from time import sleep
from random import random,randint
from threading import Thread
from queue import PriorityQueue

queue = PriorityQueue()


def producer(queue):
    print("producer running")
    for i in range(5):
        value = random()
        priority = randint(0,5)
        item = (priority,value)
        queue.put(item)
    queue.join()

    queue.put(None)
    print("producer done")

def consumer(queue):
    print("comsumer running")

    while True:
        item = queue.get()
        if item is None:
            break
        sleep(item[1])
        print(item)
        queue.task_done()
    print("consumer done")

producer = Thread(target=producer, args=(queue,))
producer.start()

consumer = Thread(target=consumer,args=(queue,))
consumer.start()
producer.join()
consumer.join()