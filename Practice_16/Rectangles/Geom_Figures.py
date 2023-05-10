class Rectangle:
    def __init__(self, name, width, heith):
        self.width = width
        self.heith = heith
        self.name = name
    def get_width(self):
        return self.width
    def get_heith(self):
        return self.heith
    def calc_Area(self):
        return self.width * self.heith

# r0 = Rectangle(width=8, heith=4)
# print(r0.calc_Area())

class Square:
    def __init__(self, side):
        self.side = side
    def area_Square(self):
        return self.side ** 2
class Round:
    def __init__(self, r):
        self.r = r
    def area_Round(self):
        return (self.r ** 2)*3.14

