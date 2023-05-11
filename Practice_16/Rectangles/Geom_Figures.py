# import necessary modules
import unittest
# import pytest
# import pytest_check as check
# import pytest_ordering as ordering

# class declaration
class Rectangle:
    """This is class for any Rectangle"""
    #  define the structure of class using __init__ method
    def __init__(self, width:int = 3, heith:int = 3):
        self.width = width
        if width <= 0:
            raise ValueError
        self.heith = heith
        if heith <= 0:
            raise ValueError
    # getter for class attribute 'width'
    def get_width(self):
        return self.width
    # getter for class attribute 'height'
    def get_heith(self):
        return self.heith
    # getter for calculating the area
    def calc_Area(self):
        return self.width * self.heith
    def __str__(self):
        return f"""
        Фигура: Rectangle

        Width Rectangle = {self.width}
        Heith Rectangle = {self.heith}

        Area = {self.width * self.heith}
        # check for negative values of sides
class Square(Rectangle):
    """This is class for any square"""
    # choose the parent class of the subclass
    def __init__(self, width:int = 3, height:int = 3):
        super().__init__(width, height)
    def get_width(self):
        return self.width
    def get_heith(self):
        return self.heith
    def calc_Area(self):
        return self.width * self.heith
    # method for display a string
    def __str__(self):
        print(f'Сторона квадрата: {self.side}')
class Round(Rectangle):
    def __init__(self, r: int = 3):
            # To inherit members use super ()
        super().__init__(r)
        self.r = r
    # override __str__ method for a new Round class
        if self.r <= 0:
            raise ValueError
    def __str__(self):
    # summarize the area of round
    def calc_Area(self):
        super().__init__()
# create a test class that inherits unittest.TestCase
class TestGetArea(unittest.TestCase):
    """Test structure Rectangle class"""
    def test_area_rec(self):
        r0 = Rectangle(3, 4)
        assert r0.calc_Area() == 12
    def test_area_squ(self):
        s0 = Square(4, 4)
        assert s0.calc_Area() == 16
    def test_area_round(self):
        cl = Round(3)
        pret  = cl.calc_Area()
        assert abs(pret - 28.25) < 0.00001

if __name__ == '__main__':
    unittest.main()
