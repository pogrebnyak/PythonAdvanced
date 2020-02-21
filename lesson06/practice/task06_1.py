class MyList():

    def __init__(self, *args):
        self._my_list = []
        for i in args:
            self._my_list = self._my_list + [i]
         
    def append(self, value):
       self._my_list += [value]

    def insert(self, index, value):
        self._my_list = self._my_list[0:index] + [value] + self._my_list[index:len(self._my_list)] 
        
    def remove(self, value):
        flag = True
        for index, j in enumerate(self._my_list):
            if value == j:
                self._my_list = self._my_list[0:index] + self._my_list[index + 1:len(self._my_list)]
                flag = False
        if flag:
            raise ValueError('list.remove(x): x not in list')
                           
    def pop(self, index=None):
       if index == None:
            index = len(self._my_list) - 1
       result = self._my_list[index]
       self._my_list = self._my_list[0:index] + self._my_list[index + 1:len(self._my_list)]
       if not result:
           raise IndexError('pop index out of range')
       return result 
         
    def clear(self):
        self._my_list = []

    def __iter__(self):
        self._start = 0
        return self

    def __next__(self):
        self._end = len(self._my_list)
        if self._start < self._end:
            self._start += 1
            return self._my_list[self._start-1]
        raise StopIteration()

    def __add__(obj1, obj2):
        for i in obj2:
          obj1.append(i)
        return obj1  
    
    def __str__(self):
        return str(self._my_list)

a = MyList(2,7,8,4,5)
b = MyList('3','77','one','two')
c = MyList()
print(c)
print(a,b)
a.insert(3,'13')
print(a,b)
a.pop(0)
print(a,b)
print(a + b)



    
