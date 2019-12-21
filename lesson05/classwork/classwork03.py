from threading import Thread

class MyThread(Thread):

    def __init__(self, args, daemon, name):
        self._arg = args
        super().__init__(daemon=daemon, name=name)

    def run(self):
        print('Working in a thread')

for i in range(100):
    MyThread(1, False, f'name-{i}').start()