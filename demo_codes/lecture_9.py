"""
This module is a demo code for lecture 8

At this lecture we cover

    - pip
    - requirements.txt
    - standard libraries
        - os
        - sys
        - argparse
        - datetime, time

    - Exceptions
        - raising
        - handling
        - creating

    - recursion (intro)

Materials
    -

    also:
    -
 Group projects
    - Stacks, Queues, Dequeues
    - Linked Lists
    - Trees
    - Maps and Hash Tables
    - Search Trees
    - Sorting and Selection
    - Heaps and B-trees (DB indexing)
"""

### exceptions (errors)
# handling, creating, raising
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/tutorial/errors.html


# # # handling
# # documentation example
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# ## add else case
# from math import sqrt
#
# while True:
#     try:
#         x = int(input("Please enter a positive number: "))
#         print(x)
#         if x <= 0:
#             raise Exception
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#     else:
#         print(f"Square root of your number is {sqrt(x)}")
#         break
#     finally:
#         print("We successfully handled an exception")

# ## create an exception
# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass
#
# class InputError(Error):
#     """Exception raised for errors in the input.
#
#     Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """
#
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.
#
#     Attributes:
#         previous -- state at beginning of transition
#         next -- attempted new state
#         message -- explanation of why the specific transition is not allowed
#     """
#
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message

# ## raise an exception
# from lecture_7_exceptions import InputError

# try:
# 	raise InputError("Input Error", "Please check your message")
# finally:
# 	print("We raised an error")
