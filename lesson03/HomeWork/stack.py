from collections import deque

class Stack:    #LIFO

    def __init__(self):
        self.my_stack = deque()

    def put_stack(self, a):
        self.my_stack.append(a)

    def get_stack(self):
        try:
            get_item = self.my_stack.pop()
        except IndexError:
            return f'Стек пуст'
        return get_item

    def __str__(self):
        return f'{self.my_stack}'

class Queue(Stack):    #FIFO

    def get_stack(self):
        try:
            get_item = self.my_stack.popleft()
        except IndexError:
            return f'Очередь пуста'
        return get_item


d = Stack()
d.put_stack('1')
d.put_stack('2')
d.put_stack('3')
d.put_stack('4')
d.put_stack('5')
print(d)
print(d.get_stack())
print(d.get_stack())
print(d.get_stack())
print(d.get_stack())
print(d.get_stack())
print(d.get_stack())
print(d)

d2 = Queue()
d2.put_stack('1')
d2.put_stack('2')
d2.put_stack('3')
d2.put_stack('4')
d2.put_stack('5')
print(d2)
print(d2.get_stack())
print(d2.get_stack())
print(d2.get_stack())
print(d2.get_stack())
print(d2.get_stack())
print(d2.get_stack())
print(d2)






