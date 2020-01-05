class Starter:

    def __init__(self, start, end):
        self._start = start
        self._end = end

class MyIter:

    def __init__(self,start,end):
        self._starter = Starter(start, end)


    def __iter__(self):
        return self._starter.__iter__()

    def __next__(self):
        if self._starter._start < self._starter._end:
            self._starter_start += 1
            return self._starter._start
        raise StopIteration()


obj = MyIter(0,4)
obj_iter  = iter(obj)
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))

for i in obj:
    print(i)

