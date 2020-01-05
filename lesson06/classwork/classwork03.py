import random

class Randomizer:

    def __init__(self,steps):
        self._steps = steps
        self._current_step = 0
        self._value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._corrent_step <= self._steps:
            self._value += random.random()
            self._current_step += 1
        else:
            raise StopIteration()
        return self._value

a = Randomizer(5)

for i in a:
    print(i)
