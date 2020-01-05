class MyIter:

    def __init__(self,start,end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start
        raise StopIteration()


obj = MyIter(0,4)
obj_iter  = iter(obj)
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))

for i in obj:
    print(i)

