class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  def __repr__(self):
    return 'Rectangle(width={}, height={})'.format(self.width,self.height)
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * self.width +  2 * self.height
  def set_height(self,height):
    self.height = height
  def set_width(self,width):
    self.width = width
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  def get_picture(self):
    picture = ""
    if (self.height > 50 or self.width > 50):
      return "Too big for picture."
    for i in range(self.height):
      picture += "*" * self.width + "\n"
    return picture
  def get_amount_inside(self,obj):
    return self.get_area() // obj.get_area()

class Square(Rectangle):
  def __init__(self,width):
    super().__init__(width,width)
  def __repr__(self):
    return 'Square(side={})'.format(self.width)
  def set_side(self,width):
    self.width = width
    self.height = width 
