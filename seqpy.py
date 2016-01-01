from collections import Sequence

class ExpandingSequence(Sequence):
    """A container class to add methods to the generator functions.

    :param name: Sequence
    :type name: a function that acts as a generator

    :Example:

    The following example uses a wrapper function primes() to construct
    an object called primes that will generate the prime numbers.
    See ducumentation on primes for examples of how to use it.

    >>> def primes():
    >>>     return ExpandingSequence(get_primes())
    >>> primes = primes()
    """

    def __init__(self, it):
        """Class initialiser.

        :param name: it
        :type name: iterator.
        """
        self.it = it
        self._cache = []

    def __getitem__(self, index):
        """Gets the next value from the generator function.

        :param name: index.
        :type name: int.
        :returns:  num -- the next value in the sequence
        """
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]

    def __len__(self):
        """Finds the length of the sequence.

        :param name: None
        :returns:  int -- the length of the sequence.

        :Example:

        >>> primes = primes()
        >>> primes[5]
        >>> len(primes)
        6
        """
        return len(self._cache)

    def seq(self):
        """Constructs a list of the sequence.

        :param name: None
        :returns:  list -- contains the values of the sequence

        :Example:

        >>> primes = primes()
        >>> primes[5]
        >>> primes.seq()
        [2, 3, 5, 7, 11]
        """
        return self._cache

    def isa(self, num):
        """Gets the next value from the generator function.

        :param name: num.
        :type name: int.
        :returns:  bool -- True is num is in the sequence

        :Example:

        To check whether 19 is a happy number

        >>> happys = happys()
        >>> happys.isa(19)
        True
        """
        while self._cache[-1] < num:
            self._cache.append(next(self.it))
        if num in self._cache:
            return True
        else:
            return False

def intersection(*args):
    """Finds numbers common to two or more sequences.

    :param name: args.
    :type name: list -- of lists.
    :returns:  list -- containing numbers common to all sequences

    :Example:

    To find numbers that are both happy and prime

    >>> happys = happys()
    >>> primes = primes()
    >>> happys[100]
    >>> primes[100]
    >>> intersection(happys.seq(), primes.seq())
    [7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293, 313,
    331, 367, 379, 383, 397, 409, 487]
    """
    A = []
    for arg in args:
        A.append(set(arg))

    A = reduce(lambda x,y: x & y,A)
    A = list(A)
    A.sort()
    return A





def get_primes():
    """Generator to find the prime numbers

    This uses the seive of Erathosens algorithm

    :param name: None
    :returns:  int -- the next prime number in the sequence.
    :raises: AttributeError, KeyError

    :Example:

    This is called by using the wrapper function primes() to the
    ExpandingSequence class.

    >>> primes = primes()
    >>> primes[5]
    >>> primes.seq()
    >>> len(primes)
    11
    [2, 3, 5, 7, 11]
    5
    """
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1


def get_squares():
    """Generator to find the square numbers


    :param name: None
    :returns:  int -- the next square number in the sequence.
    :raises: AttributeError, KeyError

    :Example:

    This is called by using the wrapper function squares() to the
    ExpandingSequence class

    >>> squares = squares()
    >>> squares[5]
    >>> squares.seq()
    >>> len(squares)
    16
    [0, 1, 4, 9, 16]
    5
    """
    candidate = 0
    while True:
        yield candidate*candidate
        candidate +=1


def get_powers(n):
    """Generator to find the powers of a number


    :param name: n
    :param type: int -- the value of the power to be used e.g. x^n
    :returns:  the next number in the sequence

    :Example:

    This is called by using the wrapper function

    >>> powers = powers(3)
    >>> powers[5]
    >>> powers.seq()
    >>> len(powers)
    81
    [1, 3, 9, 27, 81]
    5
    """
    candidate = 0
    while True:
        yield candidate**n
        candidate +=1


def get_recs(n, a, b):
    """Generator to find arbitrary recursive sequences.

    These are seuences that add the previous two terms in the sequence
    to get the next term. For example Fibonacci numbers
    The first two terms in the sequence are 0, 1
    Adding these two together gives the third term 1
    To get the next term add the last two
    1+1 = 2
    1+2 = 3
    2+3 = 5

    :param name: n
    :param type: int -- the nth number of the sequence
    :param name: a
    :param type: int -- the first term in the sequence
    :param name: b
    :param type: int -- the second term in the sequence
    :returns:  the next number in the sequence

    :Example:

    This is called by using the wrapper function

    >>> fibs = fibs(1)
    >>> fibs[5]
    >>> fibs.seq()
    >>> len(fibs)
    3
    [0, 1, 1, 2, 3]
    5
    """
    while True:
        yield a
        a,b,n = b,a+b,n-1


def get_happys():
    """Generator to find the happy numbers


    :param name: None
    :returns:  the next happy number in the sequence

    :Example:

    This is called by using the wrapper function

    >>> happys = happys(3)
    >>> happys[5]
    >>> happys.seq()
    >>> len(happys)
    19
    [1, 7, 10, 13, 19]
    5
    """
    def test_happy(n):
        past = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in past:
                return False
            past.add(n)
        return True
    candidate = 1
    while True:
        if test_happy(candidate):
            yield candidate
        candidate +=1

def get_mults(n):
    """Generator to find multiples of a number


    :param name: n
    :param type: int -- multiples of n
    :returns:  the next multiple of n

    :Example:

    This is called by using the wrapper function

    >>> multss = mults(3)
    >>> mults[5]
    >>> mults.seq()
    >>> len(mults)
    6
    [0, 3, 6, 9, 12]
    5
    """
    candidate = 0 
    while True:
		if candidate % n == 0:
			yield candidate
		candidate += 1

def get_mults(a, d):
    """Generator to find an arithmetic sequence


    :param name: a
    :param type: int -- first number of sequence
    :param name: d
    :param type: int -- common difference of sequence
    :returns:  a, a+d, a+2d ...

    :Example:

    This is called by using the wrapper function

    >>> ariths = ariths(2, 3)
    >>> ariths[5]
    >>> ariths.seq()
    >>> len(ariths)
    14
    [2, 5, 8, 11, 14]
    5
    """
    candidate = a 
    while True:
		yield candidate
		candidate +=d

################# Wrapper Functions #########################
def primes():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_primes())

def squares():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_squares())

def powers(n):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_powers(n))

def recs(n, a, b):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_recs(n, a, b))


def fibs(n):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_recs(n, 0, 1))

def happys():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_happys())
    
def mults(n):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_mults(n))
    
def evens():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_mults(2))
    
def ariths(a, d):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_ariths(a, d))

def odds():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_ariths(1, 2))
    
   
# happys = happys()
# primes = primes()
# happys[100]
# primes[100]
# print intersection(happys.seq(), primes.seq())
