from nose import with_setup
from nose.tools import raises
from seqpy import *

############ setup and teardown functions #############


def setup_module(module):
    print "setup module"


def setup_primes():
    global primes
    primes = primes()
    primes[10]


def setup_squares():
    global squares
    squares = squares()
    squares[25]


def setup_powers():
    global powers


def setup_fibs():
    global fibs


def setup_recs():
    global recs


def setup_happys():
    global happys



############# primes test ################

@with_setup(setup_primes)
def test_primes_0():
    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[5] == 13


def test_primes_seq():
    assert primes.seq()[:7] == [2, 3, 5, 7, 11, 13, 17]


def test_primes_len():
    assert len(primes) == 11


def test_primes_isa():
    assert primes.isa(5) == True
    assert primes.isa(8) == False
    assert primes.isa(50) == False

@raises(TypeError)
def test_primes_raises_type_error():
    primes[0.5]


############# squares test ################

@with_setup(setup_squares)
def test_squares_0():
    assert squares[0] == 0
    assert squares[1] == 1
    assert squares[5] == 25


def test_squares_seq():
    assert squares.seq()[:11] == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_squares_len():
    assert len(squares) == 26


def test_squares_isa():
    assert squares.isa(16) == True
    assert squares.isa(13) == False
    assert squares.isa(50) == False


@raises(TypeError)
def test_squares_raises_type_error():
    squares[0.5]
############ powers test ################

@with_setup(setup_powers)
def test_powers_0p0():
    global powers0
    powers0 = powers(0)
    assert powers0[0] == 'undefined'
    assert powers0[1] == 0
    global powers1
    powers1 = powers(1)
    assert powers1[1] == 1
    assert powers1[2] == 1


def test_powers_3_seq():
    global powers3
    powers3 = powers(3)
    powers3[4]
    assert powers3.seq() == [0, 1, 8, 27, 64]


def test_powers_len():
    global powers7
    powers7 = powers(7)
    powers7[32]
    assert len(powers7) == 33


def test_primes_isa():
    assert powers7.isa(128) == True
    assert powers3.isa(127) == False

@raises(TypeError)
def test_powers_raises_type_error():
    powers7[0.5]

"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
