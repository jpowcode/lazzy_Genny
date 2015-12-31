from nose import with_setup
from seqpy import *

############ setup functions #############


def setup_module(module):
    print "setup module"
    
def setup_primes():
    print " "
    print "Setup primes function"
    global primes
    primes = primes()
    
def setup_squares():
    print " "
    print "Setup squares function"
    global squares
    squares = squares()
     
#def teardown_module(module):
#    print "teardown_module"
    
#def my_teardown_function():
#    print "teardown function"
    
############# primes test ################

@with_setup(setup_primes)
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

@with_setup(setup_squares)
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
    global powers0 
    powers0 = powers(0)
    assert powers0[0] == 'undefined'
    
    
def test_powers_1p1():
    global powers1 
    powers1 = powers(1)
    assert powers1[1] == 1


def test_powers_3_seq():
    global powers3 
    powers3 = powers(3)
    powers3[4]
    assert powers3.seq() == [0, 3, 9, 27, 83]


def test_powers_len():
    global powers7 
    powers7 = powers(7)
    powers7[32]
    assert len(powers7) == 33



"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
