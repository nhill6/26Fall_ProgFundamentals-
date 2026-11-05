class Square:
    def __init__(self,height):
        self.height = height
    def area(self):
        return self.height * self.height

square1 = Square(6)
square2 = Square(8)

print(square1.area())
print(square2.area())