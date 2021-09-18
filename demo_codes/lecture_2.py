"""
# This module is a demo code for lecture code
"""


#####################################
#           Identifiers, Operators
#####################################

# Identifier is a name to distinguish a Python object
# A reminder: in Python everything is an object(or at least can be expressed as an object)
# Identifiers can start with "a-z, A-Z, _" characters and be followed by a "a-z, A-Z, _, 0-9" characters
# A reminder: Python is case sensitive

# print() is python function that takes an object parameter and when called prints the value on the terminal
# not to be confused with system output or interactive prompt

#######################
# 		Numbers
#######################

# print(1)
# print(type(1))
# print(type(1.0))
# print(type(2+7j))

# print("a string")
# print('a string') # though there may be some differences between single and double quotes when using literals

# now lets assign a variable
# integer_1 = 10
# integer_2 = 3
#
# print(integer_1+integer_2) # addition
# print(integer_1-integer_2) # subtraction
# print(integer_1*integer_2) # multiplication
# print(integer_1/integer_2) # division

# print(type(integer_1+integer_2)) 
# print(type(integer_1-integer_2)) 
# print(type(integer_1*integer_2)) 
# print(type(integer_1/integer_2)) # quotient is ALWAYS a float as integers are transformed to floats before division
# 								 # this is a feature of dynamic typing

# other numeric operations
# print(integer_1//integer_2) # floor division
# print(integer_1%integer_2) # remainder of division
# print(-integer_1) # negated

########################
#		Boolean
########################

# These data types are used to boolean algebra operations, and are also memory efficient

# a_bool = True
# b_bool = False

# print(type(a_bool))
# print(bool(1))
# print(bool(0))
# print(bool(''))

# False objects are
# 1. constants: None, False
# 2. zero-like objects 
# 3. empty containers

#####################
# Boolean operations
# and, or, not
# any()
# all()

# print(not b_bool)
#####################

# Now let's combine knowledge of Numbers and Booleans

##################################
# Comparison operators
# 	< 		- less than
# 	> 		- greater than
# 	<= 		- less than or equal
# 	>= 		- greater than or equal
# 	== 		- equal
# 	!= 		- not equal
# 	is 		- is identical to
# 	is not 	- is not identical to
##################################


# id() function
# difference between being identical and being equal
# print(2 == (4-2))
# print(2 is (4-2))

# print(2 == (4.-2))
# print(2 is (4.-2))

# Bitwise operations
# As we know computers work bitwise and all operations are eventually divided to bitwise operations
# Though python supports bitwise operator for integers
# First an integer is translated to the binary form
# Then and operators(like AND, NOT, etc) are applied
# this topis is OPTIONAL and we are not going to cover

############################################################################################
#################		      container-like data types 				 ###################
# mutable and immutable objects

# sequence types: list, tuple

# a = [1,2,3,4]
# print(a[0])
# a.append(5)
# print(a)
# b = (1,2,3,4)

# text or string sequence types: string
# name = "Max"

# set types: set, frozenset

# set1 =  set([12,2,3,4,5,3])
# print(set1)

# mapping types:  dict
# names = {"max": 4, "bob": 3, "max":5}
# print(names)




