
import math as H

class Rectangle(object):        #定义长方形
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

    
class Square(Rectangle):        #定义正方形
    def __init__(self, width):
        self.width  = width
        self.height = width

        
class Ellipse(object):        #定义椭圆
    def __init__(self, m, n):
        self.m = m
        self.n = n
        
    def area(self):
        return H.pi*self.m*self.n

    
class Circle(Ellipse):        #定义圆
    def __init__(self, radius):
        self.m = radius
        self.n = radius

        
def compute_area(shapes):
    return sum(item.area() for item in shapes)


shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]
total_area=compute_area(shapes)
print(total_area)
  

    

