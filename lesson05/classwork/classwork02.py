from threading import Thread
import time

def testing_threads():
    print('Func called')
    time.sleep(0.1)

#paralel
thread_list = []
start = time.time()
for i in range(20):
    t = Thread(target=testing_threads, name=f'MyThread-{i}', daemon=True)
    thread_list.append(t)

t = Thread(target=testing_threads, daemon=False, args=(10, ))
t.start()

print('I am the MAIN')