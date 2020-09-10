# Mikaela Berg 
# Chp2.1-2.3 Exercies 
# R = Reinforcemnts 
# C = Creative 

# R-2.1 Give three examples of life-critical software applications.

# R-2.2 Give an example of a software application in which adaptability can mean
# the difference between a prolonged lifetime of sales and bankruptcy.

# R-2.3 Describe a component from a text-editor GUI and the methods that it encapsulates.

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.

# R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.

# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.

# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account
# to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.

# R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?
# R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.

# R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.

# R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
# a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
# Explain how the Vector class definition can be revised so that this syntax
# generates a new vector.

# R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression v 3 returns a new vector with coordinates that are 3
# times the respective coordinates of v.

# R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
# class of Section 2.3.3, to provide support for the syntax v 3. Implement
# the rmul method, to provide additional support for syntax 3 v.

# R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression u v returns a scalar that represents the dot product of
# the vectors, that is, Σdi
# =1 ui · vi.

# R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer
# d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates
# <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it produces
# a vector with coordinates based on that sequence.

# R-2.16 Our Range class, from Section 2.3.5, relies on the formula
# max(0, (stop − start + step − 1) // step)
# to compute the number of elements in the range. It is not immediately evident
# why this formula provides the correct calculation, even if assuming
# a positive step size. Justify this formula, in your own words.

# R-2.17 Draw a class inheritance diagram for the following set of classes:
    # • Class Goat extends object and adds an instance variable tail and
    # methods milk( ) and jump().
    # • Class Pig extends object and adds an instance variable nose and
    # methods eat(food) and wallow( ).
    # • Class Horse extends object and adds instance variables height and
    # color, and methods run() and jump( ).
    # • Class Racer extends Horse and adds a method race( ).
    # • Class Equestrian extends Horse, adding an instance variable weight
    # and methods trot( ) and is trained( ).


# C-2.25 Exercise R-2.12 uses the mul method to support multiplying a Vector
# by a number, while Exercise R-2.14 uses the mul method to support
# computing a dot product of two vectors. Give a single implementation of
# Vector. mul that uses run-time type checking to support both syntaxes
# u v and u k, where u and v designate vector instances and k represents
# a number.

# C-2.26 The SequenceIterator class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The first call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.