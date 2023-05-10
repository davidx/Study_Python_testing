from Geom_Figures import Rectangle, Square, Round

r_2 = Rectangle(name='first_rect',width=3, heith=4)
r_3 = Rectangle(name='scnd_rect',width=12,heith=5)

square_1, square_2 = Square(5), Square(4)
rnd_1 = Round(4)
figures = [r_2, r_3, square_2, square_1, rnd_1]

for fig in figures:
      if isinstance(fig, Square):
            print(f'Площадь квадрата - {fig.area_Square()}')
      elif isinstance(fig, Rectangle):
            print(f'Площадь прямоугольника {fig.name} - {fig.calc_Area()}')
      elif isinstance(fig, Round):
            print(f'Площадь круга - {fig.area_Round()}')
      else:
            print('There are no figures')
