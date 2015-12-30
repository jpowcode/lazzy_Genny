from seqpy import *

############# primes test ################


@with_setup(my_setup_function, my_teardown_function)
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


############ powers test ################


def test_powers_0p0():
    assert powers(0)[0] == 0


def test_powers_1p1():
    assert powers(1)[1] == 1


def test_primes_5p0():
    assert powers(5)[0] == 0


def test_powers_3_seq():
    powers(3)[4]
    assert powers.seq() == [0, 3, 9, 27, 83]


def test_powers_len():
    powers(7)[32]
    assert len(powers) == 33



"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
