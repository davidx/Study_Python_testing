from Geom_Figures import Rectangle, Square

# sq_test = Square(int(input("введите сторону квадрата: ")))
# print(sq_test.area_Square())
class SquareException(Exception):
    pass
class NonPositiveDigitException(SquareException):
    def __init__(self, sq_value, mess='Wrong value'):
        self.sq_value = sq_value
        self.mess = mess
        super().__init__(self.mess)

try:
    sq_value = Square(int(input("введите сторону квадрата: ")))
    if sq_value.side == 0:
        raise NonPositiveDigitException(sq_value)
except ValueError:
     print(f'Wrong type of value')
except NonPositiveDigitException as error:
    print(error)
else:
    print(sq_value.area_Square())