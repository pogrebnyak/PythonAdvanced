from collections import deque

class Stack:    #LIFO

    def __init__(self):
        self.my_stack = deque()

    def push_stack(self, a):
        self.my_stack.append(a)

    def pop_stack(self):
        if self.size_stack():
            return self.my_stack.pop()
        else:
            return 'Стек пуст'

    def size_stack(self):
        return len(self.my_stack)

    def __str__(self):
        return f'{self.my_stack}'

class Queue:    #FIFO

    def __init__(self):
        self.my_queue = deque()

    def push_queue(self, a):
        self.my_queue.append(a)

    def pop_queue(self):
        if self.size_queue():
            return self.my_queue.popleft()
        else:
            return ('Очередь пуста')

    def size_queue(self):
        return len(self.my_queue)

    def __str__(self):
        return f'{self.my_queue}'




d = Stack()
d.push_stack('1')
d.push_stack('2')
d.push_stack('3')
d.push_stack('4')
d.push_stack('5')
print(f'Стек: {d}')
print(f'Размер стека: {d.size_stack()}')
print()
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d)
d2 = Queue()
d2.push_queue('1')
d2.push_queue('2')
d2.push_queue('3')
d2.push_queue('4')
d2.push_queue('5')
print(f'Очередь: {d2}')
print(f'Размер очереди: {d2.size_queue()}')
print()
print(d2.pop_queue())
print(d2.pop_queue())
print(d2.pop_queue())
print(d2.pop_queue())
print(d2.pop_queue())
print(d2.pop_queue())
print(d2)






