class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius

circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.area())
print(circle2.area())