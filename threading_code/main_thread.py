from time import sleep
from threading import current_thread
from threading import Thread


def run():
    thread = current_thread()
    print(f"Deamon thread: {thread.daemon}")


thread =Thread(target=run)

thread.start()

sleep(1)
