import unittest # import third-party modules
from typing import Union, Optional
############################################################################
class Rectangle: # declaration class
    """This is class for any Rectangle
    Первые три строки __init__ определяют конструктор класса
    и определяют две переменные для проверки. Тело конструктора
    в некоторых языках конструктора называется инициализацией
    объекта.
    Это простой метод __init__ (), который обрабатывает вход в конструктор
    и инициализирует экземпляр объекта.
    """
    # Private fields ########################################################
    # Свойства или атрибуты класса Rectangle
    width: Union[int, float] = 3  # data fields contain 3 by default
    heith: Union[int, float] = 3  # data fields contain 3 by default

    # Methods ###############################################################
    #  define the structure of class using __init__ method
    def __init__(self, width:int = 3, heith:int = 3):

        # Initializes properties
        # In this step we assign values to the instance variables

        # first initialize the width
        self.width = width
        # second initialize the height
        self.heith = heith

        # Check for negative or zero
        if width <= 0:
            raise ValueError
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
    def calc_area(self):
        return self.width * self.heith
    # method for display a string
    def __str__(self):
        print(f'Сторона квадрата: {self.side}')
class Round(Rectangle):
    """This is class for any circle"""
    def __init__(self, r: int = 3):
            # To inherit members use super ()
            super().__init__(r)
        self.r = r
        if self.r <= 0:
            raise ValueError
    # override __str__ method for a new Round class
    def __str__(self):
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
