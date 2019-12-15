class Dot:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_z(self, z):
        self._z = z

    def get_z(self):
        return self._z

    def __str__(self):
        return (f'({self._x}, {self._y}, {self._z})')

    def __add__(obj1, obj2):
        return Dot(
            obj1._x + obj2._x,
            obj1._y + obj2._y,
            obj1._z + obj2._z
        )

    def __sub__(obj1, obj2):
        return Dot(
            obj1._x - obj2._x,
            obj1._y - obj2._y,
            obj1._z - obj2._z
        )

    def __mul__(obj1, obj2):
        return Dot(
            obj1._x * obj2._x,
            obj1._y * obj2._y,
            obj1._z * obj2._z
        )

    def __truediv__(obj1, obj2):
        return Dot(
            obj1._x / obj2._x,
            obj1._y / obj2._y,
            obj1._z / obj2._z
        )
    def __neg__(self):
        return Dot(-self._x, -self._y, -self._z)





h1 = Dot(1,2,3)
h2 = Dot(2,3,4)
h1.set_x(5)
h1.set_y(6)
h1.set_z(7)
print(h1, f' x = {h1.get_x()}')
print(h2, f' z = {h2.get_z()}')

h3 = h1 + h2
print(h3)
h4 = h1 - h2
print(h4)
h5 = h1 * h2
print(h5)
h6 = h1 / h2
print(h6)
h7 = Dot(3, -4, 2)
print(-h7)


