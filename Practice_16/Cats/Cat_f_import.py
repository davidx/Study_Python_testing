from Pets import Pet

class Cat(Pet):
    def __init__(self,name='',
                 species='', gender=None,
                 breed='', age=0, reg_num=None, status_code=None):
       Pet.__init__(self, name, species, gender, breed, age, reg_num, status_code)

baron = Cat(name='Baron', age=2, breed='Сибирская', status_code='Забирают')
vano = Cat('Skoda', age=4, breed='Сиам', gender='male', status_code='out of home')

print('---')
baron.get_status()
print('---')
vano.get_main_info()
print('---')
baron.get_name()