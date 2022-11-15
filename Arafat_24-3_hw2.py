class A:
    def __init__(self, number):
        self.number = number
    def __add__(self,other):
        return self.number + other.number
class B:
    def __init__(self, number):
        self.number = number

    def __sub__(self, other):
        return self.number - other.number
class C:
    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        return self.number * other.number
class D:
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        return round(self.number / other.number, 4)
class E(A, B, C, D):
    def __init__(self, number):
        super().__init__(number)
#A.__init__(self, number, number1)
#B.__init__(self, number, number1)
#C.__init__(self, number, number1)
#D.__init__(self, number, number1)
a = E(2)
b = E(4)
print(a + b)
print(a - b)
print(a * b)
print(a / b)



