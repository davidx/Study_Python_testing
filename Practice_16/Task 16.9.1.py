class Triangle:
    """A class representing a triangle with a name, height, and base."""

    def __init__(self, name: str, h: float, base: float):
        self.name = name
        self.h = h
        self.base = base

    def calc_area_triang(self) -> float:
        """Calculates and returns the area of the triangle."""
        return self.h * (self.base / 2)

    def __str__(self) -> str:
        """Returns a string representation of the triangle."""
        return f'Triangle: {self.name}, {self.h}, {self.base}'

    def get_info_triang(self) -> None:
        """Prints the triangle's properties (name, height, and base)."""
        print('Данные фигуры:'
              f'
Имя: {self.name}'
              f'
высота = {self.h}'
              f'
основание = {self.base}')

triang_1 = Triangle('first', 12, 25)
# triang_1.get_info_triang()
# print(triang_1)

class Square:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def calc_area_sq(self):
        return self.side ** 2

class Client:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.last_name}. {self.city}. Балланс: {self.balance} руб"'

client_1_ivan = Client('Иван', 'Петров', 'Москва', 50)

# print(client_1_ivan)

class Guest:
    def __init__(self, name, l_name, city, pet, pet_s_name):
        self.name = name
        self.l_name = l_name
        self.city = city
        self.pet = pet
        self.pet_s_name = pet_s_name

    def __str__(self):
        return f'Имя и фамилия гостя: {self.name} {self.l_name}, город: {self.city}'

    def get_guest(self):
        return f'{self.name} {self.l_name}, г. {self.city}'

guest_1 = Guest('Петр','Первый','Тюмень','игуана','Лёша')
guest_2 = Guest('Леонид','Второй','ОМСК','Питон','Монти')
guest_3 = Guest('Вера','Третья','Чехов','тюлень','Аркадий')
List_of_guests = [guest_3, guest_2, guest_1]

# for gst in List_of_guests:
#     if isinstance(gst, Guest):
#         print(gst)

for gst in List_of_guests:
    print(gst.get_guest())
