"""
Library to experiment with mathematical sequences
Author: jpowcode
"""
from collections import Sequence
from functools import wraps
from datetime import datetime as dt
from math import factorial
from itertools import groupby, count
from multiprocessing import Pool
import sys
import logging

# detect python version
if sys.version_info[0] < 3:
    version = 2
else:
    version = 3

logging.basicConfig(format='%(message)s', level=logging.NOTSET)


def timeit(intercepted_function):
    """A decorator that intercepts a function and it's arguments *args
    and **kwargs times the duration of thefunction and then returns it
    and logs it to the terminal
    """

    @wraps(intercepted_function)
    def timer(*args, **kwargs):
        function_name = intercepted_function.func_name
        start = dt.now()
        actual_result = intercepted_function(*args, **kwargs)
        stop = dt.now()
        execution_time = stop - start
        logging.debug('Function: [{fnc}] => Took [{timed}]'
                      .format(fnc=function_name, timed=execution_time))

        return actual_result

    return timer


def genwrapper(intercepted_function):
    """A decorator to wrap the get_ functions below into a usable form
    """
    @wraps(intercepted_function)
    def wrapper(*args, **kwargs):
        actual_result = ExpandingSequence(intercepted_function(*args, **kwargs))
        return actual_result
    return wrapper


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
        """Constructs an object of type Seq of the sequence.

        :param name: None
        :returns:  list -- contains the values of the sequence

        :Example:

        >>> primes = primes()
        >>> primes[5]
        >>> primes.seq()
        [2, 3, 5, 7, 11]
        """
        return Seq(self._cache)

    def isa(self, num, limit=100):
        """Checks whether a number is in a particular sequence. Need to be
        careful with this as just because it is not in the current generated
        numbers does not mean it won't be if more numbers are generated.

        :param name: num.
        :type name: int.
        :param name: limit
        :type name: iint -- maximum number of terms to search
        :returns:  bool -- True is num is in the sequence

        :Example:

        To check whether 19 is a happy number

        >>> happys = happys()
        >>> happys.isa(19)
        True
        """

        if not self._cache:     # check if cache is empty to avoid errors
            self._cache.append(next(self.it))

        extras = limit - len(self._cache)  # check the existing length of cache
        if extras > 0:                     # generate more if needed
            for _ in range(extras+1):
                self._cache.append(next(self.it))

        if num in self._cache:
            return True
        else:
            return False


class Seq():
    """Constructs an object that holds a list and collection of methods for
    filtering and opperating on the list. The difference between this and a
    list is that it is imutable. The origonal list will not be changed. The
    generator function will output an object of this type when the .seq
    method is called
    """
    def __init__(self, seq):
        self.seq = seq

    def __str__(self):
        return str(self.seq)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'ImmutableList(' + str(self) + ')'

    def __eq__(self, other):
        if self.seq == other:
            return True
        else:
            return False

    def sort(self, cmp=None, key=None, reverse=False):
        new = list(self.seq)
        new.sort(cmp=None, key=None, reverse=False)
        return Seq(new)

    def append(self, x):
        new = list(self.seq)
        new.append(x)
        return Seq(new)

    def extend(self, L):
        new = list(self.seq)
        new.extend(list(L.seq))
        return Seq(new)

    def insert(self, i, x):
        new = list(self.seq)
        new.insert(i, x)
        return Seq(new)

    def remove(self, x):
        new = list(self.seq)
        new.remove(x)
        return Seq(new)

    def pop(self, i):
        new = list(self.seq)
        new.pop(i)
        return Seq(new)

    def index(self, x):
        new = list(self.seq)
        new.index(x)
        return Seq(new)

    def count(self, x):
        new = list(self.seq)
        return new.count(x)

    def reverse(self):
        new = list(self.seq)
        new.reverse()
        return Seq(new)

    def between(self, a, b):
        new = list(self.seq)
        if len(new) > 0:
            if version == 2:
                return Seq(filter(lambda x: a <= x <= b, new))
            else:
                # python 3 version of filter returns an itertor and we need a
                # list.
                return Seq(list(filter(lambda x: a <= x <= b, new)))
        else:
            return Seq(new)

    def list(self):
        return self.seq

    def len(self):
        return len(self.seq)

    def sum(self):
        return sum(self.seq)


class Generators():

    @genwrapper
    def squares(self):
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

    @genwrapper
    def mersennes(self):
        """Generator to find the nth Mersenne number


        :param name: None
        :returns:  the next Mersenne number in the sequence

        :Example:

        >>> mersennes = mersennes()
        >>> mersennes[4]
        >>> mersennes.seq()
        >>> len(mersennes)

        15
        [0, 1, 3, 7, 15]
        4
        """
        n = 0
        while True:
            yield 2**n - 1
            n += 1

    @genwrapper
    def merprimes(self):
        """Generator to find the nth Mercenne Prime number


        :param name: None
        :returns:  the next Mersenne Prime number in the sequence

        :Example:

        >>> merprimes = merprimes()
        >>> merprimes[10]
        >>> merprime.seq()
        >>> len(merprime)

        257
        [2, 3, 5, 7, 13, 17, 19, 31, 67, 127, 257]
        11
        """

        def isprime(n):
            if n == 1:
                return False
            dv = 2
            while dv * dv <= n:
                if n % dv == 0:
                    return False
                dv = dv + 1
            return True

        def ismerc(n):
            if not isprime(n):
                return False
            if n == 1:
                return False
            if n == 2:
                return True
            m = 2**n - 1
            x = 4
            for i in range(n-2):
                x = (x * x - 2) % m
            return x == 0

        candidate = 1

        while True:
            if ismerc(candidate):
                yield 2**candidate - 1
            candidate += 1

    @genwrapper
    def primes(self):
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

    @genwrapper
    def intersection(self, *args):
        """Finds numbers common to two or more sequences.

        :param name: args.
        :type name: list -- of lists.
        :returns:  generator -- containing numbers common to all sequences

        :Example:

        To find numbers that are both happy and prime

        >>> happys = happys()
        >>> primes = primes()
        >>> happyprimes = intersection(happys, primes)
        >>> happyprimes[100]

        [1, 7, 10, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263,
        293, 313, 331, 367, 379, 383, 397, 409, 487]
        """

        gens = []
        for gen in args:
            try:
                gen[1]

            except:
                gen = gen()
            gens.append(gen)

        candidate = 0
        while True:
            logic = True
            for gen in gens:
                logic = logic * gen.isa(candidate)
                # if one evaluates to false logic is false
            if logic:
                yield candidate

            candidate += 1

    @genwrapper
    def union(self, *args):
        """Finds numbers in either of two or more sequences.

        :param name: args.
        :type name: list -- of lists.
        :returns:  generator -- containing numbers in any of the sequences

        :Example:

        To find numbers that are both happy and prime

        >>> happys = happys()
        >>> primes = primes()
        >>> happyORprimes = union(happys, primes)
        >>> happyORprimes[10]

        [1, 2, 3, 5, 7, 10, 11, 13, 17, 19, 23]
        """

        gens = []
        for gen in args:
            try:
                gen[1]

            except:
                gen = gen()
            gens.append(gen)

        candidate = 0
        while True:
            logic = False
            for gen in gens:
                logic = logic + gen.isa(candidate)
                # if one evaluates to false logic is false
            if logic:
                yield candidate

            candidate += 1

    @genwrapper
    def consecratios(self, gen, d=2):
        """Generator to find the ratios of consecutive terms
        e.g for [t1, t2, t3, t4 ...]
        returns [t2/t1, t3/t2, t4/t3 ...]

        :param name: gen
        :param type: generator
        :param name: d
        :param type: int -- number of decimal places to round to default = 2
        :returns:  int -- the next consecutive ration in the sequence.
        :raises: AttributeError, KeyError

        :Example:

        >>> consecratios = consecratios(primes)
        >>> consecratios[4]
        >>> consecratios.seq()
        >>> len(consecratios)

        1.57
        [1.5, 1.67, 1.4, 1.57]
        5
        """
        n = 1
        try:
            gen[n]
        except:
            gen = gen()

        while True:
            gen[n]
            try:
                yield round(gen[n]*1.0/gen[n-1], d)
            except:
                yield None
            n += 1

    @genwrapper
    def every(self, gen, d):
        """Constructs a generator of the sequence but only every n items

        :param name: d
        :param type: int
        :param name: gen
        :param type: generator

        :returns:  list -- contains the values of the sequence every n items

        :Example:

        >>> palinds2 = every(palinds, 2)
        >>> primes[10]
        [1, 3, 5, 7, 9, 22, 44, 88, 101, 12]
        """
        n = 0
        try:
            gen[1]
        except:
            gen = gen()
        while True:
            if n % d == 0:
                yield gen[n]
            n += 1

    @genwrapper
    def powers(self, n):
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

    @genwrapper
    def recs(self, a, b):
        """Generator to find arbitrary recursive sequences.

        These are seuences that add the previous two terms in the sequence
        to get the next term. For example Fibonacci numbers
        The first two terms in the sequence are 0, 1
        Adding these two together gives the third term 1
        To get the next term add the last two
        1+1 = 2
        1+2 = 3
        2+3 = 5

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
        n = 0
        while True:
            yield a
            a, b, n = b, a+b, n-1

    def fibs(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.recs(0, 1)

    @genwrapper
    def happys(self):
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

    @genwrapper
    def mults(self, n):
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

    def evens(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.mults(2)

    @genwrapper
    def ariths(self, a, d):
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

    def odds(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.ariths(1, 2)

    @genwrapper
    def geoms(self, a, r):
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

    @genwrapper
    def ndigits(self, n):
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

    @genwrapper
    def facts(self):
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

    @genwrapper
    def polys(self, n):
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

    def triangs(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.polys(3)

    @genwrapper
    def sumfacts(self, dpa):
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

            if version == 2:
                for i in xrange(1, candidate):
                    if candidate % i == 0:
                        total += i
            else:
                # python 3 does not have xrange. range is equivalent
                for i in range(1, candidate):
                    if candidate % i == 0:
                        total += i

            if dpa == 'd' and total < candidate:
                yield candidate
            if dpa == 'p' and total == candidate:
                yield candidate
            if dpa == 'a' and total > candidate:
                yield candidate
            candidate += 1

    def perfs(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.sumfacts('p')

    def defics(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.sumfacts('d')

    def abunds(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        return self.sumfacts('a')

    @genwrapper
    def palinds(self):
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

    @genwrapper
    def arbfuncs(self, f):
        """Generator to find the nth term in an arbitrary function


        :param name: f
        :param type: function -- an arbitray function of the form f(n)
        :returns:  the next number in the sequence f(n)

        :Example:

        This is called by using the wrapper function get_arbfuncs
        Use the functiion f(n) = n^2 + 3n -1

        >>> f = lambda n: n**2 +3*n -1
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

    def lazcats(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        f = lambda n: (n**2 + n + 2) / 2
        return self.arbfuncs(f)

    def catnums(self):
        """A wrapper function, creates an object using ExpandingSequence
        class
        """
        f = lambda n: factorial(2*n)/(factorial(n+1)*factorial(n))
        return self.arbfuncs(f)

    @genwrapper
    def mods(self, gen, div):
        """Generator to find the nth remainder of the given generator when
        divided by div


        :param name: gen
        :param type: generator
        :param name: div
        :param type: int -- the divisor

        :returns:  the remainder of next number in the generators sequence
        when divided by div

        :Example:

        >>> fibs[10]
        >>> fibs.seq()
        >>> modfibs3 = mods(fibs, 3)
        >>> modfibs3[10]
        >>> modfibs3.seq()

        89
        [0, 1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
        1
        [0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1]
        """

        try:
            gen[1]

        except:
            gen = gen()

        n = 0
        while True:
            yield gen[n] % div
            n += 1

    @genwrapper
    def looksays(self):
        """Generator to find the look and say sequence


        :param name: None
        :returns:  the next look and say number in the sequence

        :Example:

        >>> looksays = looksays()
        >>> looksays[5]
        >>> looksays.seq()
        >>> len(looksays)

        312211
        [1, 11, 21, 1211, 111221, 312211]
        5
        """

        numberstring = 1
        while True:
            if numberstring == 1:
                numberstring = '1'
                yield 1

            else:
                numberstring = ''.join(str(len(list(g))) + k
                                       for k, g in groupby(numberstring))
                yield int(numberstring)

    @genwrapper
    def pis(self):
        """Generator to find the digits of pi


        :param name: None
        :returns:  the next digit of pi

        :Example:

        >>> pis = pis()
        >>> pis[5]
        >>> pis.seq()
        >>> len(pis)

        9
        [3, 1, 4, 1, 5, 9]
        5
        """

        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
        while True:
            if 4*q + r - t < n*t:
                yield n
                nr = 10*(r - n * t)
                n = ((10*(3*q + r))//t) - 10*n
                q *= 10
                r = nr
            else:
                nr = (2*q+r)*l
                nn = (q*(7*k)+2+(r*l))//(t*l)
                q *= k
                t *= l
                l += 2
                k += 1
                n = nn
                r = nr

    @genwrapper
    def harshads(self):
        """Generator to find the Harshad numbers


        :param name: None
        :returns:  the next Harshad number

        :Example:

        >>> harshads = harshads()
        >>> harshads[4]
        >>> harshads.seq()
        >>> len(harshads)

        8
        [1, 2, 3, 4, 5, 6, ,7]
        7
        """
        for n in count(1):
            if n % sum(int(ch) for ch in str(n)) == 0:
                yield n


class MultiThread():
    """A class to allow running generators in separate threads.

    :param name: num_threads
    :type name: int -- the number of threads to use

    :Example:

    The following example sets the primes and happys to be generated
    in seaprate threads.

    >>> G = Generators()
    >>> primes = G.primes()
    >>> happys = G.happys()
    >>> T = MultiThread(2)
    >>> T.run([primes[10000], happys[10000]])
    >>> print primes[10000]
    >>> print happys[10000]
    """
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.run_thread = self.call_gen(self)
        self.pool = Pool(self.num_threads)

    def call_gen(self, g):
        """A wrapper to run the generators when called from
        the map function
        """
        g

    def run(self, generators):
        """A class to allow running generators in separate threads.

        :param name: generators
        :type name: list -- of generators

        Example

        >>> run([primes[100], happys[100]])
        """
        self.pool.map(self.run_thread, generators)
        self.pool.close()
        self.pool.join()
