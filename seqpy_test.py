from seqpy import *


def test_primes_0():
    assert primes[0] == 2


def test_primes_1():
    assert primes[1] == 3


def test_primes_5():
    assert primes[5] == 13


def test_primes_seq():
    assert primes.seq() == [2, 3, 5, 7, 11, 13]


def test_primes_len():
    assert len(primes) == 6
