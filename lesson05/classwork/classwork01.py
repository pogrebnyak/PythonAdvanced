from threading import Thread
import time

def testing_threads():
    print('Func called')
    time.sleep(0.1)

#sync output
start = time.time()
for i in range(20):
    testing_threads()

print(time.time() - start)

#paralel
thread_list = []
start = time.time()
for i in range(20):
    t = Thread(target=testing_threads, name=f'MyThread-{i}')
    thread_list.append(t)
for i in thread_list:
    print(i.start())

print(time.time() - start)