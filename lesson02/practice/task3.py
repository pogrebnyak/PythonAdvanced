class dot:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def change_x(self,x):
        self.x = x

    def change_y(self,y):
        self.y = y

    def change_z(self,z):
        self.z = z

    def __str__(self):
        return (f'({self.x}, {self.y}, {self.z})')

    def __add__(obj1, obj2):
        return dot(
            obj1.x + obj2.x,
            obj1.y + obj2.y,
            obj1.z + obj2.z
        )

h1 = dot(1,2,3)
h2 = dot(2,3,4)
h1.change_x(5)
h1.change_y(5)
h1.change_z(5)

h3 = h1 + h2
print(h1)
print(h2)
print(h3)


