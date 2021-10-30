"""
This module is a demo code for lecture 3

At this lecture we cover
    - container-like objects (iterables)
        - sequences
            - list
            - tuple
            - strings
        - set types
            - set
            - frozenset
        - mapping types
            - dict
        * collections.abc, re.pattern, re.match
    - control flows
        - if
        - if else
        - if elif else
        - for
        * for else
        - while
        - break continue pass

    - math modules
        - math
        - random

Materials
    - https://docs.python.org/3.9/library/stdtypes.html
    - https://docs.python.org/3/library/math.html
    - https://docs.python.org/3/library/random.html

    also:
    - https://i.stack.imgur.com/GemQf.png 

"""
from typing import Sized, Hashable

object
###########################################
# 1. overview of methods and attributes
###########################################

# # example of an integer
# new_integer = 1
# print("Our integer is ", new_integer)
#
# # attributes: data is stored in the object or the class
# print("Attributes")
# real_of_new_int = new_integer.real
# imag_of_new_int = new_integer.imag
# print("Real part of the integer:", real_of_new_int)
# print("Imaginary part of the integer:", imag_of_new_int)
#
# # method: a function (an operation) that return "data"
# print("Methods")
# real_of_new_int = new_integer.__sizeof__()
# print(f"The size of our integer object is {real_of_new_int} bytes")
#
# # dir and doc functions
# # dir (or __dir__() method) function returns a list of all methods and attributes of the class instance
# # __doc__ attribute is a multiline string describing the class
#
# int_met_att = dir(new_integer)
# print(int_met_att)
#
# print(new_integer.__add__(100))
# print(new_integer.__add__("A"))  # print error
# print(new_integer.__eq__(1))
#
# print(new_integer.__doc__)

###############################
#  2. Container-like data types
###############################

# sequences: list, tuple, string

# ranks = ("2","3","4","5","6","7","8","9","10","jack", "queen", "king", "ace",)
#
# suits = (
#     "spades",
#     "hearts",
#     "diamonds",
#     "spades"
# )
#
# # sequence operations
#
# print("K" in ranks)
# print("ace" not in ranks)
# print([1,2,3] + [[4],5,6])
# print([1,2,3] * 3)
#
# # # member accessing, slicing
# print(ranks)
# print(ranks[0])
# print(ranks[-1])
# print(ranks[0:2])
# print(ranks[2:])
# print(ranks[::2])
# print(ranks[::-1])
# #
# # difference of mutable and immutable sequences - HASHING
# # accessor vs mutator methods
# # https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1200px-Hash_table_3_1_1_0_1_0_0_SP.svg.png
#
# # list operations
#
# list_example = [1,2,3]
#
# # mutator method
# list_example.append("a")
# list_example.append((1,2,3))
# list_example.extend((1,2,3))
# print(list_example)
#
#
# # sets
# set_example = {
#     "banana",
#     "apple",
#     "orange"
# }
# #
# set_example.add("pineapple")
#
# # mapping: dictionaries
#
# bl_values = {
#     "king": (10,10),
#     "ace": (1,11)
#     "1": (1,1)
# }
#
# bl_values['king']

####################
# # 3. Control-flows
####################
# a = 0
# if a == 1:
#     print("odd")
# elif a == 2:
#     print("odd")
# else:
#     pass
#
# for i in [1, 2, 3, 4, 5]:
#     if i == 2:
#         continue
#     print(i)
#     if i == 4:
#         break
# else:
#     print("_______________")
#
###############################
# 4. math and random modules
###############################
# python module - .py
#
# from math import e, sqrt
#
# print(e)
# print(sqrt(5))
