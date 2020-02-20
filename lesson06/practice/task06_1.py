class MyList():

    def __init__(self):
        self._my_list = []
        
         
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
            raise ValueError
                           
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

a = MyList()
c = MyList()
a.append('1')
a.append('2')
a.append('3')
a.append('4')
a.append('5')
c.append('1')
c.append('2')
c.append('3')
c.append('4')
c.append('5')
a.insert(3,'13')
a.pop(0)
print(a,c)
print(type(a),type(c))
print(a + c)



    
