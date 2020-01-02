# -*- coding: utf-8 -*-

#DOCS about decorators https://www.datacamp.com/community/tutorials/decorators-python

def protect_decorator(func):
    def wrapper_func(person_object, admin_password):
        if admin_password == '@dmin':
            return func(person_object)
        else:
            print('The admin password is incorrect')
    return wrapper_func

class Person:
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._surname = kwargs['surname']
        self._age = kwargs['age']

    @protect_decorator
    def get_information(self):
        print(f'My name is {self._name + " " + self._surname } and i\'m  {self._age} old year')

p1 = Person(name= 'Jesús', surname='Villamarin', age=22)

p1.get_information('wrong_password')
p1.get_information('@dmin')
