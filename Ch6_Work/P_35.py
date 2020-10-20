"""PART A: C-6.16 Modify the ArrayStack implementation so that the stack’s capacity is limited
to maxlen elements, where maxlen is an optional parameter to the
constructor (that defaults to None). If push is called when the stack is at
full capacity, throw a Full exception (defined similarly to Empty).

"""

"""PART B: P-6.35 The introduction of Section 6.1 notes that stacks are often used to provide
“undo” support in applications like a Web browser or text editor. While
support for undo can be implemented with an unbounded stack, many
applications provide only limited support for such an undo history, with a
fixed-capacity stack. When push is invoked with the stack at full capacity,
rather than throwing a Full exception (as described in Exercise C-6.16),
a more typical semantic is to accept the pushed element at the top while
“leaking” the oldest element from the bottom of the stack to make room.
Give an implementation of such a LeakyStack abstraction, using a circular
array with appropriate storage capacity. This class should have a public
interface similar to the bounded-capacity stack in Exercise C-6.16, but
with the desired leaky semantics when full.

"""


""""TODO: User creates the stack and it has max capacity, when you exceed it from push it will thorugh an exception (so brush up on it)
so instead of thorwing the excpetion pitch the last one. Leaky stack.

"""


"""
Only really can go back to 5 undoes like in chess.

"""


"""Classic calculator example opperators comes after the operands.

"""


"""Make up my own data and go past and exceed the data and be able to tell what has leaked out, if I have time
it would be nice to at any point display the contents of the stack. I can add some interactivity where the user inputs a number
and i push it on the stack (something that represents the undo function) instead of a number and I can put a letter or something,
it doesn't have to be large maybe 5 elements large.

"""