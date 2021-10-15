"""
This module is a demo code for lecture 6

At this lecture we cover

    - OOP principles
        - abstraction
        - inheritance
        - encapsulation
        - polymorphism
    - property() decorator
    - exec vs eval
    - instructions vs expressions
    - eager vs lazy evaluation
    - iterators, generators
    - open(), with and context managers
    - more special methods
    - object class (builtins.py)
    - UML diagrams

    - abstract base classes
    - metaclasses

Materials


    also:
    - MRO: https://www.geeksforgeeks.org/multiple-inheritance-in-python/
    - meta-classes: https://realpython.com/python-metaclasses/
    - ABC: https://docs.python.org/3/library/abc.html (not to be mixed with collections.abc)
    - UML cheat sheet: https://khalilstemmler.com/files/resources/umlcheatsheet.jpg
"""


#
##########################################################
# ## OO principles
# # 1. Abstraction
# # Abstraction is the concept of object-oriented programming that “shows”
# # only essential attributes and “hides” unnecessary information.
#
# class User:
#     """
#     user class for a game
#     """
#     total_users = 0
#
#     def __init__(self, nickname, password, lvl, ):
#         self.nickname = nickname
#         self.lvl = lvl
#         self.password = password
#         User.change_total_users()
#
#     @classmethod
#     def change_total_users(cls):
#         cls.total_users += 1
#
#
# class User:
#     """
#     user class for social media
#     """
#
#     def __init__(self, name, login, university, profile_pic=None):
#         self.name = name
#         self.__login = login
#         self.university = university
#         self._profile_pic = profile_pic
#
#     def __repr__(self):
#         return f"This is {self.name} from {self.university}, find him/her @ {self.__login}"
#
#     # property controls the behavior of
#     # 1.getting the attribute that is how <object.attribute> is accessed
#     # 2.setting a new value to the attribute - <object.attribute = new_value>
#     # 3.deleting the attribute - def object.attribute
#     #
#     @property  # getter
#     def profile_pic(self): return self._profile_pic
#
#     @profile_pic.setter  # setter
#     def profile_pic(self, photo_url):
#         self._profile_pic = photo_url
#
#     @profile_pic.deleter  # deleter
#     def profile_pic(self):
#         del self._profile_pic
#
#     # # other syntax
#     # def get_profile_pic(self):
#     #     return self._profile_pic
#     #
#     # def set_profile_pic(self, photo_url):
#     #     self._profile_pic = photo_url
#     #
#     # def del_profile_pic(self):
#     #     del self._profile_pic
#     #
#     # profile_pic = property(get_profile_pic, set_profile_pic, del_profile_pic, "profile pic property")
#
#
# # __repr__() method
# a_user = User("Gevorg Ghalachyan", "ggh96", "YSU")
# print(a_user)
#
# # 2. Encapsulation
# # Encapsulation is a mechanism to wrap up fields and methods together as a single unit.
# # It is the process of hiding information details and protecting data and behavior of the object.
# a_user.__login = "gevorg_ghalachyan"
# print(a_user.__login)
#
# print(a_user.profile_pic)
# a_user.profile_pic = "https://avatars.githubusercontent.com/u/32383635?s=400&u" \
#                      "=b32bf643784f3b979d3b446015d0180a290f9757&v=4 "
# print(a_user.profile_pic)
# del a_user.profile_pic
# # print(a_user.profile_pic) # will raise error, field is deleted

#################################################################
# 3. Inheritance
# Inheritance is the ability to build new classes on top of existing ones
# 4. Polymorphism
# Polymorphism is the ability of a program to detect the real class
# of an object and call its implementation even when its real
# type is unknown in the current context.
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     def __init__(self, name=None, family=None):
#         self.name = name
#         self.family = family
#
#     @abstractmethod  # must be implemented
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         super().__init__(name=None)
#
#     def make_sound(self):
#         print("Meow!")
#
#
# a_cat = Cat("Garfield")
# a_cat.make_sound()

# Method Resolution Order in Python(MRO)
# In the case of multiple inheritance, a given attribute is first searched in the current class
# if it’s not found then it’s searched in the parent classes.
# The parent classes are searched in a depth-first, left-right fashion and each class is searched once.

#
# ###########################
# # type, meta, __mro__
# class F1:
#
#     def m(self):
#         print(f"m printed in {self.__class__}")
#         print(f"m printed from F1")
#
#
# class F2(F1):
#
#     def m(self):
#         print(f"m printed in {self.__class__}")
#         print(f"m printed from F2")
#
#
# class F3(F1):
#
#     def m(self):
#         print(f"m printed in {self.__class__}")
#         print(f"m printed from F3")
#
#
# class F4_1(F2, F3):
#     pass
#
#
# class F4_2(F3, F2):
#     pass
#
#
# inst_F4_1 = F4_1()
# print(F4_1.__mro__)
# inst_F4_1.m()
#
# inst_F4_2 = F4_2()
# print(F4_2.__mro__)
# inst_F4_2.m()
#

##################################################

#
# # # iterators - __iter__(), __next__()
# # iter should return the object
# # next should return the next element
# # https://github.com/python/cpython/blob/3.10/Lib/_collections_abc.py
#
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# rev = Reverse('spam')
# for char in rev:
#     print(char)
#
#
# # generators - yield statement
# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
#
# # generator comprehension
# gen = (elem for elem in range(10) if elem % 3 == 0)
# print(gen)
# print(elem for elem in gen)
#
# # range()
# # zip()
#
#
# reverse('abc')
# print(reverse('abc'))
#
# a = reverse('abc')
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# # print(a.__next__()) # will raise StopIteration exception
#
# a = reverse('abc')
# for elem in a:
#     print(elem)

###################################
# # # context managers
# # __enter__ and __exit__ methods
# # python i/o
#
# print(open.__doc__)
# path = "../data/zen_of_python.txt"
#
# # read entire file
# file = open(path, "r")
# print(file)
# print(file.__dir__())
# text = file.read()
# print(text)
#
# # read line by line
# file = open(path, "r")
# print(file)
# for line in file:
#     print(line, end="")
#
# # open as context manager
# with open(path, "r") as file:
#     for line in file:
#         print(line, end="")
#
# # append with the context manager
# with open(path, "a") as file:
#     for num in range(5):
#         file.write("a line is added\n")
#
# # write with the context manager
# with open("../data/a_new_random_file.txt", "w") as file:
#     for num in range(5):
#         file.write("a line is added\n")