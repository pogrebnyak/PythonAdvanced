import threading
import time
import logging
import wget

urls = ('https://8i.com.ua/pic/pil01.png',
        'https://8i.com.ua/pic/pil02.png',
        'https://8i.com.ua/pic/pil03.png',
        'https://8i.com.ua/pic/pil04.png',
        'https://8i.com.ua/pic/pil05.png',
        'https://8i.com.ua/pic/pil06.png',
        'https://8i.com.ua/pic/pil07.png',
        'https://8i.com.ua/pic/pil08.png',
        'https://8i.com.ua/pic/pil09.png',
        'https://8i.com.ua/pic/pil10.png',
        )


def decorator(name_tread, bool_daem):
    def actual_decorator(func):
        def wrapper():
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            for i, url in enumerate(urls, start=1):
                my_thread = threading.Thread(target=func, name=name_tread, daemon=bool_daem, args=(name_tread, i, url,))
                threads.append(my_thread)
                my_thread.start()
            for i in threads:
                i.join()
            pass

        return wrapper

    return actual_decorator


@decorator('Поток', True)
def func(name, i, url):
    logging.info(f'Thread {name}-{i:02}: Starting download {url}')
    wget.download(url, f'.\picwget{i:02}.png')
    logging.info(f'Thread {name}-{i:02}: Download finishing')


threads = []

func()