import random

def randomizer(steps):

    current_step = 0
    value = 0
    while current_step <= steps:
        value += random.random()
        current_step += 1
        yield value

for i in randomizer(100):
    print (i)

