class Rectangle:
    def __init__(self, width, heith):
        self.width = width
        self.heith = heith

    def get_width(self):
        return self.width

    def get_heith(self):
        return self.heith
    def calc_Area(self):
        return self.width * self.heith

r0 = Rectangle(width=8, heith=4)
# print(r0.calc_Area())