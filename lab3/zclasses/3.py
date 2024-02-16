class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def _init_(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    

    
shape = Shape()
print(shape.area()) 
rect = Rectangle(4,5)
print(rect.area())