import _thread
import threading
import time

# def thread_task(thread_name, delay):
#     for count in range(1,6):
#         time.sleep(delay)
#         print(f"thread name: {thread_name} count: {count}")
#
#
# try:
#     _thread.start_new_thread(thread_task,('thread-1',1,))
#     _thread.start_new_thread(thread_task, ('thread-2', 2,))
# except:
#     print("Error: unable to start thread")
#
# while True:
#     pass


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting "+self.name)
        for count in range(1,6):
            time.sleep(3)
            print(f"thead name :{self.name} Count:{count}")
        print(f"Exiting {self.name}")


thread1 = myThread("Thread-1")
thread2 = myThread("thread-2")
thread3 = myThread("thread-3")

# print(type(thread1))
thread1.start()
time.sleep(1)
thread2.start()
thread3.start()
thread1.join()
thread2.join()
print("Exiting main thread")