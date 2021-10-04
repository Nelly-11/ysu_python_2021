"""
This module is a demo code for lecture 4

At this lecture we cover
    - functions
    - git

Materials
    - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    - https://i.redd.it/8341g68g1v7y.png
    - Michael T. Goodrich, Data Structures and Algorithms in Python - Chapter 1.5
    - git intro: https://www.youtube.com/watch?v=RGOj5yH7evk

    also:
    - some git topics: https://www.youtube.com/watch?v=Uszj_k0DGsg

"""
#############
#  FUNCTIONS
#############

# # define a function with def keyword
# # use return keyword to keep the result
# # use pass keyword as the function does nothing
# # use () to call a function
# # parameter vs argument
#
# def nothing():
#     pass
#
#
# print(nothing)
# print(type(nothing))
# nothing()
#
#
# def sqr(x):
#     return x**2
#
#
# a = sqr(4)
# print(a+1)
#
# a = 2
# a_sqr = sqr(a)
# print(a_sqr)


# # you can return multiple arguments with different options
# def degree_2_3(x):
#     return x ** 2, x ** 3
#
#
# print(degree_2_3(x=4))
#
# a, b = degree_2_3(x=4)
# print(a, b)
#
# a = degree_2_3(x=4)
# print(a)
#
# _, b = degree_2_3(x=4)
# print(b)
#########################################################


# # print first n fibonacci numbers and write a docstring
# def fib(n):
#     """
# this function return the first n fibonacci numbers
#
# parameters
# 	n - integer number
#
# returns
# 	list of first n fibonacci numbers
# 	"""
#
#     if isinstance(n, int):
#         a, b = 0, 1
#         first_n_fib = [0, 1]
#
#         for i in range(n - 2):
#             a, b = b, a + b
#             first_n_fib.append(b)
#
#         print(first_n_fib)
#
#     else:
#         print("input is not an integer")
#
#
# # lets try cases
# fib(n=5.5)
# fib(n='a')
# fib(n=10)
#
# print(fib.__doc__)
# print(dir(fib))
###########################################

# # default and positional arguments
#
# def alarm(text = "alarm message"):
# 	print(text)
#
# alarm()
# alarm(text = "new alarm message")
# alarm("another alarm message")
#
#
# def sum3(a,b,c):
# 	print(a*b+c)
#
# sum3(a=10,c=20,b=30)

# to keep in mind, all variables inside the function are local variables
# that is they are all created and used only within function block

# # immutable type example
# c = 4
#
# def foo(x = c):
# 	print(x)
# 	print(c)
#
# c = 5
# foo()
#
# # mutable type example
# c = [1,2,3,4]
#
# def foo(x = c):
# 	print(x)
# 	print(c)
#
#
# c.append(5)
# foo()

# default arguments are assigned once
# The default values are evaluated at the point of function definition in the defining scope
# so be careful with mutable arguments (or never use them)
###############################################################

# Arbitrary and keyword arbitrary arguments
# def foo(basket_num, *products, **amounts):
# 	print(f"Our basket number is {basket_num}")

# 	print("\n\t information about the items")
# 	for item in products:
# 		print(f"the basket includes {item}")
# 	print(products)

# 	print("\n\t information about the amounts")
# 	for item in amounts:
# 		print(f"the basket includes {item }: {amounts[item]}")

# 	print(amounts)

# foo(4, 'egg', 'cheese', 'jam','bacon', egg = 10, cheese = 8, bacon = 6)

# # functions are objects
# print(foo)

# # recap argument types
####################################

# local, non-local, global

# def scope_test():

#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
# 	  print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

