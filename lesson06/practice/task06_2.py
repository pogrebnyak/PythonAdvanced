# Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.

class MyDict():    


    def __init__(self, **kwargs):    #Ключи не могут быть int   
        self._kwargs = kwargs
        print(kwargs)
		
    def get(self, values, default=None):
        for i in self._kwargs:
            print(repr(i))
            if i == values:
                return self._kwargs[i]
        return default
    
    def keys(self):
        result = [x for x in self._kwargs]
        return result

    def values(self):
        result = [self._kwargs[x] for x in self._kwargs]
        return result

    def items(self):
        result = [(x, self._kwargs[x]) for x in self._kwargs]
        return result

    def __add__(obj1, obj2):     #Если ключи совпадают, затирает значением со второго объекта
        for i in obj2._kwargs:
            obj1._kwargs[i] = obj2._kwargs[i]  
        return obj1._kwargs
     

d = MyDict(d=32 , g=23, f='iuyti', kj='dfdf')
c = MyDict(df=34, g=234, thr=876, tks='fdsf')
print(d.keys())
print(d.values())
print(d.items())
print()
print(d + c)





	
