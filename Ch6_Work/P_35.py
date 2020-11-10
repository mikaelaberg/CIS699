"""
--------------------------PART A DONE----------------------------------------
PART A: C-6.16 Modify the ArrayStack implementation so that the stack’s
capacity is limited to maxlen elements, where maxlen is an optional parameter
to the constructor (that defaults to None). If push is called when the stack
is at full capacity, throw a Full exception (defined similarly to Empty).
--------------------------PART A DONE----------------------------------------

--------------------------PART B DONE----------------------------------------
PART B: P-6.35 The introduction of Section 6.1 notes that stacks are
often used to provide “undo” support in applications like a Web browser or
text editor. While support for undo can be implemented with an unbounded
stack, many applications provide only limited support for such an undO
history, with a fixed-capacity stack. When push is invoked with the stack
at full capacity, rather than throwing a Full exception (as described in
Exercise C-6.16), a more typical semantic is to accept the pushed element
at the top while “leaking” the oldest element from the bottom of the stack
to make room. Give an implementation of such a LeakyStack abstraction,
using a circular array with appropriate storage capacity. This class should
have a public interface similar to the bounded-capacity stack in Exercise
C-6.16, but with the desired leaky semantics when full.
--------------------------PART B DONE----------------------------------------

---------------------Meeting Notes 10/22/20----------------------------------
-->User creates the stack and it has max capacity, when you exceed it from
push it will thorugh an exception (so brush up on it)so instead of thorwing
the excpetion pitch the last one. Leaky stack.

-->Only really can go back to 5 undoes like in chess.

-->Classic calculator example opperators comes after the operands.

-->Make up my own data and go past and exceed the data and be able to tell
what has leaked out, if I have time it would be nice to at any point display
the contents of the stack. I can add some interactivity where the user
inputs a number and i push it on the stack (something that represents the
undo function) instead of a number and I can put a letter or something, it
doesn't have to be large maybe 5 elements large.
-----------------------------------------------------------------------------

--------------------------PART C DONE ---------------------------------------
PART C: C-7.30 Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT
using a singly linked list for storage.
--------------------------PART C DONE ---------------------------------------

"""

#--------------------------PART A --------------------------------------------
class Empty(Exception):
    """
    Generating and initalizing the Empty class for the ArrayStack class.
    """
    pass


class Full(Exception):
    """
    Generating and initalizing the Full class for the ArrayStack class.
    """
    pass

class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underling storage

    From the textbook on page 233 6.1 Stacks.
    """

    def __init__(self, maxlen = None):
        """
        Creating an empty stack.
        """
        self._data = []    #nonpublic list instance
        self.maxlen = maxlen

    def __len__(self):
        """
        Return the number of elements in the stack
        """
        return len(self._data)

    def isEmpty(self):
        """
        Return True if the stack is empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element e to the top of the stack
        """
        if self.maxlen is not None and len(self) == self.maxlen:
            raise Full('The stack is full')
        self._data.append(e)     #new item stores at end of list

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.

        Rain Empty exception if the stack is empty.
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data[-1]       #the last item in the list

    def pop(self):
        """
        Remove and retrun the element from the top of the stack (i.e., LIFO)

        Raise Empty exception if the stack is empty.
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data.pop()     #remove last item from list


#--------------------------PART B --------------------------------------------
class LeakyStack(ArrayStack):
    """
    For the 'undo' when a new element is pushed into the stack when at
    max capacity it will leak out into the leaky stack.
    """
    def __init__(self, capacity = 20):
        self._data = [None]*capacity
        self._capacity = capacity
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, value):
        self._data[(self._front + self._size)%len(self._data)] = value
        if self._size == self._capacity:
            self._front += 1
        else: self._size += 1

    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        ans = self._data[(self._front + self._size -1)%len(self._data)]
        self._data[(self._front + self._size -1)%len(self._data)] = None
        self._size -= 1
        return ans


#--------------------------PART C --------------------------------------------

class SinglyLinked_LeakyStack(ArrayStack):
    """
    Similar to the LeakyStack in Part B but this time useing a singly linked stack structure.
    """

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, size = 0):

        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)      #Create and link a new node
        self._size += 1


    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element                  #top of stack is at the head of list

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next                #bypass the former top node
        self._size -= 1
        return answer


stackA = ArrayStack()

for i in range(12):
    try:
        stackA.push(i)
        print(stackA.top())
    except Full as e:
        print(e)


# ----------------Part B---------------------------------------
undo = LeakyStack()
for i in range(6):
    undo.push(i)

print ('Leakiness check')
while not undo.isEmpty():
    print(undo.pop())

# ----------------Part C---------------------------------------
singleLinkedUndo = SinglyLinked_LeakyStack()
for i in range(8):
    singleLinkedUndo.push(i)

print ('Leakiness check')
while not singleLinkedUndo.is_empty():
    print(singleLinkedUndo.pop())




