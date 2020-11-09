#Ch 7.1 Singularly Linked List


#Inserting an Element at the Head of a Singly Linked List
#Pseudo code:
# Algrothim add_first(L,e):
#     newest = Node(e)            #Create new node instance storing reference to element e
#     newest.next = L.head        #Set new node's next to reference the old head node
#     L.head = newest             #set variable head to reference the new node
#     L.size = L.size + 1         #increment the node count

#Inserting an Element at the Tail of a Singly Linked List
#Pseudo code:
# Algrothim add_last(L,e):
#   newest = Node(e)              # Create new node instance sotring reference to elemnet e
#   newest.next = None            #Set new node's next to reference to None object
#   L.tail.next = newest          #make old tail node point to new node
#   L.tail = newest               #set variable tail to reference the new node
#   L.size = L.size + 1           #increment the node count

#Removing an element from a Singly Linked List
#Pseudo Code:
#Algrothim remove_first(L):
#   if L.head is None then:
#       Indicate and error: the list is empty
#   L.head = L.head.next         #Make head point to next node (or None)
#   L.size = L.size -1           #decrement the node count

class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage.
    """
#------------------------nested _Node class------------------------------
class _Node:
    """
    Lightweight nonpublic class for storing a singly linked node.
    """

    __slots__ = '_element' , '_next'        #streamline memory usage

    def __init__(self, element, next):      #initialize node's fields
        self._element = element             #reference to user's element
        self._next = next                   #reference to next node

#------------------------stack methods------------------------------------
    def __init__(self):
        """
        Create an empty stack.
        """
        self._head = None                  #references to the head node
        self._size = 0                     #number of stack elements

    def __len__(self):
        """
        Return the number of elements in the stack.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the stack is empty
        """
        return self._size == 0

    def push(self,e):
        """
        Add elements e to the top of the stack.
        Args:
            e ([any]): [element]
        """
        self._head = self._Node(e, self._head)      #Create and link a new node
        self._size += 1

    def top(self):
        """
        Return (but does not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element                  #top of stack is at the head of list

    def pop(self):
        """
        Remove and return the element from the top of a stack (i.e LIFO)

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next                #bypass the former top node
        self._size -= 1
        return answer


class LinkedQueue:
    """
    FIFO queue implementation using a singly linked list for storage
    """
    class _Node:
        def __init__(self, element, next):      #initialize node's fields
            self._element = element             #reference to user's element
            self._next = next                   #reference to next node\


    def __init__(self):
            """
            Create an empty queue.
            """
        self._head = None
        self._tail = None
        self._size = 0                          #number of the queue elements

    def __len__(self):
        """
        Return the number of the elements in the queue.
        """
        return self._size

    def is_empty(self):
        """
        return self._size ==0
        """
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (ie. FIFO)
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():             #special case as queue is empty
            self.tail = None            #removed head had been tail
        return answer

    def enqueue(self,e):
        """
        Add an element to the back of the queue.
        """
        newest = self._Node(e,None)         #node will be new tail node
        if self.is_empty():
            self._head = newest             #special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                 #update reference to tail node
        self._size += 1

#-------------------------------------------------------------------------------------
#Ch 7.2 Circularly Linked list

class CircularQueue:
    """
    Queue implementation using circularly linked list for storage.
    """

    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element' , '_next'        #streamline memory usage

    def __init__(self):
        """
        Create an empty queue
        """

        self._tail = None           #will represent tail of queue
        self._size = 0              #number of queue elements

    def __len__(self):
        """
        Return the number of elements in the queue.
        """

        return self.size

    def is_empty(self):
        """
        Return True of the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return (but do not have to remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (ie FIFO).

        Raise Empty exception if the queue is empty
        """
        is self.is_empty():
            raise EMpty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:                         # removing only element
            self._tail = None                       # queue becomes empty
        else:
            self._tail._next = oldhead._next        # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        """
        Add an element to the back of the queue.
        """
        newest = self._Node(e, None)               # node will be new tail node
        if self.is_empty():
            newest._next = newest                  # initialize circularly
        else:
            newest._next = self._tail._next        # new node points to head
            self._tail._next = newest              # old tail points to new node
        self._tail = newest                        # new node becomes the tail
        self._size += 1

        def rotate(self):
            """
            Rotate front element to the back of the queue.
            """
            is self._size > 0:
                self._tail = self._tail._next     # old head becomes new tail

#-------------------------------------------------------------------------------------
#Ch 7.3 Doubly Linked list:

#sentinels (or guards) do not store elements of the primary sequence, they are the header and trailer
#of a doubly linked list

class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation.
    """
    class _Node:
        """
        Lightweight, nonpublic class for storing a doubly linked node.
        """
        __slots__ = '_element', '_prev', '_next'            # streamline memory

        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                         # user's element
            self._prev = prev                               # previous node reference
            self._next = next                               # next node reference

    def __init__(self):
        """
        Create an empty list
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the list.
        """
        return self._size

    def is_empty(self):
        """
        Return True if list is empty
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing node and return new node
        """
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return its element
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element


class LinkedDeque(_DoublyLinkedBase):                       # note the use of inheritance
    """
    Double-ended queue implementation based on a doubly linked list.
    """

    def first(self):
        """
        Return (but do not remove) the element at the front of the deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element                  # real item just after the header

    def last(self):
        """
        Return (but do not remove) the element at the back of the deque.
        """

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._prev._element                  # real item just before the trailer

    def insert_first(self, e):
        """
        Add an element to the front of the deque
        """
        self._insert_between(e, self._header, self._header.next)           # after header

    def insert_last(self,e):
        """
        Add an element to the back of the deque
        """
        self._insert_between(e, self._trailer._prev, self._trailer)       # before trailer

    def delete_first(self):
        """
        Remove an return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)                      # use inherited method

    def delete_lst(self):
        """
        Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        is self.is_empty():
            raise Empty("Deque is empty")
        return self.delete_node(self._trailer._prev)                    # use inherited method