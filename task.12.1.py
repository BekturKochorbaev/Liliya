class Shape:
    def __init__(self, a):
        self.a = a

    def perimetr(self):
        pass

class Circle(Shape):
    def perimetr(self):
        return self.a * 3.14

circle1 = Circle(2)
print(circle1.perimetr()) # 6.28 sm

class Rectangle(Shape):
     def __init__(self, a, b):
         super().__init__(a)
         self.b = b

     def perimetr(self):
         return (self.a + self.b) * 2

rec1 = Rectangle(4, 5)
print(rec1.perimetr()) # 19 sm

class Triangle(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def perimetr(self):
        return self.a * self.b * self.c

tr1 = Triangle(4, 5, 6)
print(tr1.perimetr()) # 120 sm