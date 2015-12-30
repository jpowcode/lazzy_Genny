from seqpy import *

############# primes test ################


def test_primes_0():
    assert primes[0] == 2


def test_primes_1():
    assert primes[1] == 3


def test_primes_5():
    assert primes[5] == 13


def test_primes_seq():
    primes[6]
    assert primes.seq() == [2, 3, 5, 7, 11, 13, 17]


def test_primes_len():
    primes[9]
    assert len(primes) == 10

############# squares test ################


def test_squares_0():
    assert squares[0] == 0


def test_squares_1():
    assert squares[1] == 1


def test_primes_7():
    assert squares[5] == 25


def test_squares_seq():
    squares[10]
    assert squares.seq() == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_squares_len():
    squares[25]
    assert len(squares) == 26
