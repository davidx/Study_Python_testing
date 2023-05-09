class Pet:
    def __init__(self, name='',
                 species='', gender=None,
                 breed='', age=0, reg_num=None, status_code=None):
        self.name = name
        self.species = species
        self.gender = gender
        self.breed = breed
        self.age = age
        self.reg_num = reg_num
        self.status_code = status_code


    def get_main_info(self):
        print(f'Питомец - {self.name}'
               f'\nвозраст - {self.age}'
               f'\nПол - {self.gender}'
               f'\nПорода - {self.breed}'
               f'\nСтатус - {self.status_code}')
    def get_name(self):
        print(f'Имя питомца - {self.name}')
    def get_status(self):
        print(f'Имя Питомца - {self.name}'
              f'\nРегистрационный номер Питомца - {self.reg_num}'
              f'\nСтатус питомца - {self.status_code}')

