import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"
    
circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")