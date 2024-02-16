class Shape:
    def area(self):
        return 0

class Square(Shape):
    def _init_(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    

    
shape = Shape()
print(shape.area()) 
square = Square(4)
print(square.area())