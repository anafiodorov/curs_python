print("Curs 3")
import random

while True:
    all_choices = [i for i in range(10)]
    random_choice = random.choice(all_choices)
    if random_choice % 3 == 0:
        break
print(f'Selected choice was {random_choice}')

for i in all_choices:
    if i % 2 != 0:
        continue
    print(f'Numar par {i}')

if True:
    pass
else:
    print('This is False')


# FUNCTII#
def my_function(a, b):
    c = a + b
    # print(c)


print(my_function(1, 2))


def my_function_1(a, b):
    c = a + b
    return c


print(my_function_1(1, 2))


def my_function_append(list_param):
    # ca sa nu modificam lista initiala, ii facem o copie
    list_param = list(list_param)
    list_param.append(4)


my_list = [1, 2, 3]
my_function_append(my_list)
print(my_list)


def my_function_args(param_1, param_2, *args, **kargs):
    # primul parametru, precedat cu *, are rolul de a prelua toți parametrii poziționali nedeclarați în semnătura funcției, dar transmiși în
    # momentul apelării acesteia. Ei se vor regăsi într-o listă în ordinea în care au fost transmiși.
    # al doilea parametru, precedat cu **, are rolul de a prelua toți parametrii cheie:valoare nedeclarați în semnătura funcției, dar transmiși în momentul apelării acesteia. Ei se vor regăsi într-un dicționar.
    print(param_1)
    print(param_2)
    print(args)
    print(kargs)


my_function_args(0, 2, 3, 6, -5, 'abc', name="ion")


# RECURSIVITATE#
def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(7))

# EXCEPTII#

my_var = input('Introduceti un nr:')
try:
    my_int = int(my_var)
except ValueError as e:
    print('Please insert an integer! The following error happened: ', e)
else:
    print('We are here because no exception was fired')
finally:
    print('We execute this block no matter what')

# NAMESPACES#

print(dir(__builtins__))


# NAMESPACE - GLOBAL#
def my_function_namespaces():
    global msg
    msg = 'salut'
    print(msg)


my_function_namespaces()
print(msg)


# NAMESPACES - ENCLOSING#

def my_function_enclosing():
    def my_second_function():
        msg = 'Yololo'
        print(f'my_second_function: {msg}')

    msg = "Hello world"
    my_second_function()
    print(f"my_function: {msg}")


my_function_enclosing()

# MODULES#

from my_package.my_second_module import *

print(my_var)
print(my_var_2)


# OOP#

# CLASSES#

class Coordinate(object):
    """O coordonata e compusa din x si y"""

    def __init__(self, x, y):
        """Setam valorile x si y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Returnam self ca si string"""
        return f"{self.x}, {self.y}"

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def get_x(self):
        return self.x

    def set_y(self, new_y):
        self.y = new_y


a = Coordinate(1, 2)
print(a)
origin = Coordinate(0, 0)
print(origin.distance(a))

origin.set_y(2)
print(origin)


# MOSTENIREA#

class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


animal_1 = Animal(20)
print(animal_1)
animal_1.set_name("Gogu")
print(animal_1.name)


class Cat(Animal):

    def speak(self):
        print("meow")

    def __str__(self):
        return "cat" + ":" + str(self.age)


animal_2 = Animal(30)
print(animal_2)
animal_3 = Cat(40)
animal_3.speak()
print(animal_3)
animal_3.set_name("Pis")
print(animal_3.name)