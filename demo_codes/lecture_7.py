"""
This module is a demo code for lecture 8

At this lecture we cover
    - iterators, generators
    - open(), with and context managers
    - UML diagrams
    - modules, packages
    - create a package
    - project
    - pip
    - requirements.txt
    - standard libraries
    - Exceptions
        - raising
        - handling
        - creating

Materials
    -

    also:
    -

"""

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

# # ################################################
# # modules
# from a_module import another_function
# from homework.answer.lecture3 import another_function_2
# from lecture_6 import foo, NewClass
#
# foo()
# a = NewClass()
#
# from lecture_6 import *
#
# a = AnotherClass()
# print(a.sqrt1p(9))
#
# # absolute and relative paths
# another_function()
# another_function_2()

# # packages

# from lecture6.module_ import Mod11
#
# a = Mod11()
#
# from lecture6.module_2 import Mod22
#
# a = Mod22()
#
# from lecture6 import *
#
# a = Mod12
#
# # ## __name__ == "__main__"
#
# print(__name__)
# foo12()
# foo22()

# built-in modules and packages
# https://docs.python.org/3.8/library/index.html

