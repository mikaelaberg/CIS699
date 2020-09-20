
''' R-2.18 Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.

R-2.19 When using the ArithmeticProgression class of Section 2.4.2 with an increment
of 128 and a start of 0, how many calls to next can we make
before we reach an integer of 263 or larger?'''


#R-2.18

class Progression:
    """Iterator producting a generic progression
    Default iterator produces the whole number 0,1,2...
    """

    def __init__(self, start=0):
        """Initalize current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value
        This should be overwritten by a subclass to a customize progression
        By convention, if current is set to None, this designates the
        end of the finite progression."""
        self._current += 1
    
    def __next__(self):
        """Return the next elemnet or else rasie StopIteration error. """
        if self._current is None:       #our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      #record current value to return
            self._advance()             #advance to prepare for the next time
            return answer               #return the answer

    def __iter__(self):
        """By convention, and iterator must return itself as an iterator"""
        return self

    def print_progression(self,n):
        """Print next n values of the progression."""
        print(''.join(str(next(self))for j in range(n)))


class FibonacciProgression(Progression):
    """Iterator producting a generalized Fibonacci progression"""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.
        first       the first term of the progression(default 0)
        second      the second term of the progression(defualt 1)
        """
        super().__init__(first)
        self._prev = second = first

    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current




