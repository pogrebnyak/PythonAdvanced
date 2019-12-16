class FromMeta:
    def hello(self):
        print ('Hello')

class UpperCaseMetaclass(type):

    def __new__(cls, name, base, attrs):
        for i in range(5):
            base = (FromMeta,)
            attrs.update({'var_' + str(i): i})
        return super().__new__(cls, name, base, attrs)

class Inherited():
    pass

class MiddleWare(metaclass=UpperCaseMetaclass):
    pass

class MyClass(Inherited, MiddleWare):

    _attribute_of_class = 'Attr'
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(dir(MyClass))
MyClass(1, 2).hello()




