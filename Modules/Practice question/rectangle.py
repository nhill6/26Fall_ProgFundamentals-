class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle1 = Rectangle(4,5)
rectangle2 = Rectangle(6,8)
print(rectangle1.area())
print(rectangle2.area())