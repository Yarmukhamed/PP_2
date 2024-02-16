import math
class Point() :

    dist = 0
    def _init_(self,x,y):
        self.x = x
        self.y = y
    def show(self) :
        print(self.x,self.y)
    def move(self,x2,y2) :
        self.x = x2
        self.y = y2
    def dist(self,poi) :
        return math.sqrt(((self.x-poi.x)*2 + (self.y-poi.y)*2))
point = Point(4,3)
point2 = Point(5,6)
print(point.dist(point2))
point.show()
point.move(5,6)
point.show()