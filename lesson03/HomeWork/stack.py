from collections import deque

class Stack:    #LIFO

    def __init__(self):
        self.my_stack = deque()

    def push_stack(self, a):
        self.my_stack.append(a)

    def pop_stack(self):
        if len(self.my_stack):
            return self.my_stack.pop()
        else:
            return 'Стек пуст'

    def size_stack(self):
        return len(self.my_stack)

    def __str__(self):
        return f'{self.my_stack}'

class Queue:    #FIFO

    def __init__(self):
        self.my_stack = deque()

    def push_Queue(self, a):
        self.my_stack.append(a)

    def pop_Queue(self):
        if len(self.my_stack):
            return self.my_stack.pop()
        else:
            return ('Очередь пуста')

    def size_Queue(self):
        return len(self.my_stack)

    def __str__(self):
        return f'{self.my_stack}'




d = Stack()
d.push_stack('1')
d.push_stack('2')
d.push_stack('3')
d.push_stack('4')
d.push_stack('5')
print(d)
print(d.size_stack())
print()
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d.pop_stack())
print(d)
#
d2 = Queue()
d2.push_Queue('1')
d2.push_Queue('2')
d2.push_Queue('3')
d2.push_Queue('4')
d2.push_Queue('5')
print(d2)
print(d2.size_Queue())
print()
print(d2.pop_Queue())
print(d2.pop_Queue())
print(d2.pop_Queue())
print(d2.pop_Queue())
print(d2.pop_Queue())
print(d2.pop_Queue())
print(d2)






