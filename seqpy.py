from collections import Sequence
from functools import partial


class ExpandingSequence(Sequence):
    """A container class to add methods to the generator functions below
    """
    def __init__(self, it):
        self.it = it
        self._cache = []

    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]

    def __len__(self):
        return len(self._cache)

    def seq(self):
        return self._cache


def get_primes():
    "Simple lazy Sieve of Eratosthenes"
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1


def get_squares():
    "square numbers"
    candidate = 0
    while True:
        yield candidate*candidate
        candidate +=1


def get_powers(n):
    "Arbitrary powers numbers"
    candidate = 0
    while True:
        yield candidate**n
        candidate +=1

primes = ExpandingSequence(get_primes())
squares = ExpandingSequence(get_squares())

powers = 0
def powers(n):
	global powers
	powers = ExpandingSequence(get_powers(2))

powers(2)
print squares[5]
print squares.seq()
print powers[3]
print len(powers)
#print powers(2)[1]
#print powers(2)[2]
#print powers(2).seq
