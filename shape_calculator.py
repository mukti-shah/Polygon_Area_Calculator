class Rectangle:

    def __init__(self,w,h):
        self.width = w
        self.height = h
      
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,w):
        self.width = w

    def set_height(self,h):
        self.height = h
      
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        pict = ''
        for i in range(self.height):
            pict += ('*' * self.width)
            pict+='\n'

        if len(pict)>100:
          return "Too big for picture."
        return pict
    
    
    def get_amount_inside(self, fit):
        return (self.get_area()//fit.get_area())
        
        
class Square(Rectangle):
    
    def __init__(self, s):
        self.width = s
        self.height = s
        
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, s):
        self.width = s
        self.height = s