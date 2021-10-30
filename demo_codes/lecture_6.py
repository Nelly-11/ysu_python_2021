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
    - more special methods
    - object class (builtins.py)

    - abstract base classes
    - metaclasses

Materials
    - Michael T. Goodrich, Data Structures and Algorithms in Python - Chapter 2
    - Python Programming: An Introduction to Computer Science - Chapter 10.1-5
    - Dusty Phillips, Python 3 Object-oriented Programming

    also:
    - MRO: https://www.geeksforgeeks.org/multiple-inheritance-in-python/
    - meta-classes: https://realpython.com/python-metaclasses/
    - ABC: https://docs.python.org/3/library/abc.html (not to be mixed with collections.abc)
    - UML cheat sheet: https://khalilstemmler.com/files/resources/umlcheatsheet.jpg
    - name mangling: https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
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

# Note differences between __var__ _var and __var
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
from math import sqrt

def foo():
    print(1)

class NewClass:
    pass


class AnotherClass:

    @staticmethod
    def sqrt1p(n):
        return sqrt(n) + 1
