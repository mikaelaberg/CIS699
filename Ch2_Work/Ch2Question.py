# Mikaela Berg 
# Chp2.1-2.3 Exercies 
# R = Reinforcemnts 
# C = Creative 
# P = Project

# Skipping R-2.1 Give three examples of life-critical software applications.
 
# Skipping R-2.2 Give an example of a software application in which adaptability can mean
# the difference between a prolonged lifetime of sales and bankruptcy.

# Skipping R-2.3 Describe a component from a text-editor GUI and the methods that it encapsulates.

'''R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.'''

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

'''R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer
d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates
<4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces
a vector with coordinates based on that sequence.'''

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

''' R-2.18 Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.

R-2.19 When using the ArithmeticProgression class of Section 2.4.2 with an increment
of 128 and a start of 0, how many calls to next can we make
before we reach an integer of 263 or larger?'''

# R-2.20 What are some potential efficiency disadvantages of having very deep inheritance
# trees, that is, a large set of classes, A, B, C, and so on, such that
# B extends A, C extends B, D extends C, etc.?

# R-2.21 What are some potential efficiency disadvantages of having very shallow
# inheritance trees, that is, a large set of classes, A, B, C, and so on, such
# that all of these classes extend a single class, Z?

# R-2.22 The collections.Sequence abstract base class does not provide support for
# comparing two sequences to each other. Modify our Sequence class from
# Code Fragment 2.14 to include a definition for the eq method, so
# that expression seq1 == seq2 will return True precisely when the two
# sequences are element by element equivalent.

# R-2.23 In similar spirit to the previous problem, augment the Sequence class with
# method lt , to support lexicographic comparison seq1 < seq2.





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

# C-2.27 In Section 2.3.5, we note that our version of the Range class has implicit
# support for iteration, due to its explicit support of both len
# and getitem . The class also receives implicit support of the Boolean
# test, “k in r” for Range r. This test is evaluated based on a forward iteration
# through the range, as evidenced by the relative quickness of the test
# 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
# more efficient implementation of the contains method to determine
# whether a particular value lies within a given range. The running time of
# your method should be independent of the length of the range.

# C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process month
# method that models the completion of a monthly cycle. Modify the class
# so that once a customer has made ten calls to charge in the current month,
# each additional call to that function results in an additional $1 surcharge.

# C-2.29 Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer
# is assigned a minimum monthly payment, as a percentage of the
# balance, and so that a late fee is assessed if the customer does not subsequently
# pay that minimum amount before the next monthly cycle.

# C-2.30 At the close of Section 2.4.1, we suggest a model in which the CreditCard
# class supports a nonpublic method, set balance(b), that could be used
# by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the
# CreditCard and PredatoryCreditCard classes accordingly.

# C-2.31 Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the previous
# two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults.

# C-2.32 Write a Python class that extends the Progression class so that each value
# in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your constructor
# should accept an optional parameter specifying the start value, using
# 65,536 as a default.


# P-2.33 Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the first derivative of that polynomial.

# P-2.34 Write a Python program that inputs a document and then outputs a barchart
# plot of the frequencies of each alphabet character that appears in
# that document.

# P-2.35 Write a set of Python classes that can simulate an Internet application in
# which one party, Alice, is periodically creating a set of packets that she
# wants to send to Bob. An Internet process is continually checking if Alice
# has any packets to send, and if so, it delivers them to Bob’s computer, and
# Bob is periodically checking if his computer has a packet from Alice, and,
# if so, he reads and deletes it.

"""P-2.36 Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears)."""

# P-2.37 Write a simulator, as in the previous project, but add a Boolean gender
# field and a floating-point strength field to each animal, using an Animal
# class as a base class. If two animals of the same type try to collide, then
# they only create a new instance of that type of animal if they are of different
# genders. Otherwise, if two animals of the same type and gender try to
# collide, then only the one of larger strength survives.

# P-2.38 Write a Python program that simulates a system that supports the functions
# of an e-book reader. You should include methods for users of your
# system to “buy” new books, view their list of purchased books, and read
# their purchased books. Your system should use actual books, which have
# expired copyrights and are available on the Internet, to populate your set
# of available books for users of your system to “purchase” and read.

# P-2.39 Develop an inheritance hierarchy based upon a Polygon class that has
# abstract methods area( ) and perimeter( ). Implement classes Triangle,
# Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
# class, with the obvious meanings for the area( ) and perimeter( ) methods.
# Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle,
# and Square, that have the appropriate inheritance relationships. Finally,
# write a simple program that allows users to create polygons of the
# various types and input their geometric dimensions, and the program then
# outputs their area and perimeter. For extra effort, allow users to input
# polygons by specifying their vertex coordinates and be able to test if two
# such polygons are similar.