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

    def __str__(self):
        itname = eval(self.it.__name__)
        return itname.__doc__

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

    def every(self, n):
        """Constructs a list of the sequence but only every n items

        :param name: n
        :param type: int
        :returns:  list -- contains the values of the sequence every n items

        :Example:

        >>> primes = primes()
        >>> primes[7]
        >>> primes.every(2)
        [2, 5, 11, 17]
        """
        return self._cache[::n]

    def between(self, a, b):
        """Constructs a list of the sequence between the values a and b.

        :param name: a
        :param type: int -- lower bound
        :param name: b
        :param type: int -- upper bound
        :returns:  list -- contains the values of the sequence between
                            a and b

        :Example:

        >>> primes = primes()
        >>> primes[5]
        >>> primes.seq().between(3, 7)
        [3, 5, 7]
        """
        if not self._cache:     #check if cahce is empty to avoid errors
            self._cache.append(next(self.it))
        while self._cache[-1] < b:
            self._cache.append(next(self.it))
        return filter(lambda x: a <= x <= b, self._cache)


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
        if not self._cache:     #check if cahce is empty to avoid errors
            self._cache.append(next(self.it))
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

    A = reduce(lambda x, y: x & y, A)
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
        candidate += 1


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
        candidate += 1


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
        a, b, n = b, a+b, n-1


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
        candidate += 1


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


def get_ariths(a, d):
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
        candidate += d


def get_geoms(a, r):
    """Generator to find a geometric sequence


    :param name: a
    :param type: int -- first number of sequence
    :param name: r
    :param type: int -- common ratio of sequence
    :returns:  a, ar, ar^2 ...

    :Example:

    This is called by using the wrapper function

    >>> geoms = geoms(2, 3)
    >>> geoms[5]
    >>> geoms.seq()
    >>> len(geoms)
    32
    [2, 4, 8, 16, 32]
    5
    """
    candidate = a
    while True:
        yield candidate
        candidate *= r


def get_ndigits(n):
    """Generator to find numbers with n digits


    :param name: n
    :param type: int -- number of digits
    :returns:  list with n digit numbers

    :Example:

    This is called by using the wrapper function

    >>> ndigits = ndigits(4)
    >>> ndigits[5]
    >>> ndigits.seq()
    >>> len(ndigits)
    32
    [1001, 1002, 1003, 1004]
    5
    """
    candidate = 10**(n-1)
    while candidate < 10**n:
        yield candidate
        candidate += 1


def get_facts():
    """Generator to find the factorial numbers


    :param name: None
    :returns:  the next factorial number in the sequence

    :Example:

    This is called by using the wrapper function get_facts

    >>> facts = facts(3)
    >>> facts[5]
    >>> facts.seq()
    >>> len(facts)
    120
    [1, 1, 2, 6, 24, 120]
    6
    """
    candidate = 0
    n = 2
    while True:
        if candidate == 0:
            yield 1
            candidate = 1
        else:
            yield candidate
            candidate *= n
            n = n + 1


def get_polys(n):
    """Generator to find polygonal numbers


    :param name: n
    :param type: int -- number of edges in polygon
    :returns:  list of polygonal numbers order n

    :Example:

    This is called by using the wrapper function polys(3) for pentagonal
    numbers

    >>> polys = polys(5)
    >>> polys[3]
    >>> polys.seq()
    >>> len(polys)
    22
    [1, 5, 12, 22]
    4
    """
    candidate = 1
    m = 0
    while True:
        yield candidate
        candidate += n - 1 + m*(n - 2)
        m += 1


def get_perfs(dpa):
    """Generator to find the perfect, abundant or deficient numbers


    :param name: dpa
    :param type: string -- set as d for deficient, p for perfect and
                            a for abundant
    :returns:  the next deficient, perfect or abundant number
                in the sequence

    :Example:

    This is called by using the wrapper function get_perfs

    >>> perfs = perfs('p')
    >>> perfs[4]
    >>> perfs.seq()
    >>> len(perfs)
    8128
    [6, 28, 496, 8128]
    4
    """
    candidate = 1
    while True:
        total = 0
        for i in xrange(1, candidate):
            if candidate % i == 0:
                total += i
        if dpa == 'd' and total < candidate:
            yield candidate
        if dpa == 'p' and total == candidate:
            yield candidate
        if dpa == 'a' and total > candidate:
            yield candidate
        candidate += 1


def get_palinds():
    """Generator to find pallindromic numbers


    :param name: None
    :returns:  the next pallindromic in the sequence

    :Example:

    This is called by using the wrapper function get_palinds

    >>> palinds = palinds()
    >>> palinds[15]
    >>> palinds.seq()
    >>> len(palinds)
    77
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77]
    16
    """
    candidate = 1
    while True:
        NumListFor = list(str(candidate))
        NumListBack = list(str(candidate))
        NumListBack.reverse()
        if NumListFor == NumListBack:
            yield candidate
        candidate = candidate + 1
        
     
def get_arb_funcs(f):
    """Generator to find the nth term in an arbitrary function


    :param name: f
    :param type: function -- an arbitray function of the form f(n)
    :returns:  the next number in the sequence f(n)

    :Example:

    This is called by using the wrapper function get_arbfuncs
	Use the functiion f(n) = n^2 + 3n -1
	
	>>> f = lambda n: n**2 +3n -1
    >>> arbfuncs = arbfuncs(f)
    >>> arbfuncs[4]
    >>> arbfuncs.seq()
    >>> len(arbfuncs)
    8128
    [-1, 3, 9, 17]
    4
    """
    n = 0
    while True:
		yield f(n)
		n += 1


"""
------------------------------------------------------------------------------
Wrapper Functions
------------------------------------------------------------------------------
"""


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


def geoms(a, r):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_geoms(a, r))


def ndigits(n):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_ndigits(n))


def facts():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_facts())

def polys(n):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_polys(n))

def triangs():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_polys(3))


def perfs():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_perfs('p'))


def defics():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_perfs('d'))


def abunds():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_perfs('a'))


def palinds():
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_palinds())
    
    
def abfuncs(f):
    """A wrapper function, creates an object using ExpandingSequence
    class
    """
    return ExpandingSequence(get_arbfuncs(f))
