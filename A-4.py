class Rectangle():
    def __init__(self, l, w):
        self.width = w
        self.height = l

    def rectangle_area(self):
        return self.height * self.width

newRectangle = Rectangle(5, 10)
print(f"Dimesions of the rectangle - Length : %d Width : %d" % 
      (newRectangle.height, newRectangle.width))
print(f"Area of rectangle :", newRectangle.rectangle_area())