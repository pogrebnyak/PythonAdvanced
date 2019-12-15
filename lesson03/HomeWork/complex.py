class MyComplex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real}+{self.imag}j' if self.imag >= 0 else f'{self.real}-{-self.imag}j'

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return MyComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.imag * other.imag,
                         self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return MyComplex((self.real * other.real + self.imag * other.imag) / ((other.real ** 2) + (other.imag ** 2)),
                         (other.real * self.imag - self.real * other.imag) / ((other.real ** 2) + (other.imag ** 2)))


s1 = MyComplex(3,2)
print(s1)
s2 = MyComplex(1,2)
print(s2)
print()
s3 = s1 + s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s1 * s2
print(s3)
s3 = s1 / s2
print(s3)
