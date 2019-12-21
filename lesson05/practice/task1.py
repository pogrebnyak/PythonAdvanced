import threading
import time
import logging


def decorator(name, bool_daem):
    def actual_decorator(func):
        def wrapper():
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            my_thread = threading.Thread(target=func, name=name, daemon=bool_daem, args=(name,))
            my_thread.start()
            #my_thread.join()
            pass
        return wrapper
    return actual_decorator


@decorator('Поток-1', False)
def func(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    logging.info(f'Thread {name}: finishing')

func()
