from nose import with_setup
from nose.tools import raises
from seqpy import *

############ setup and teardown functions #############


def setup_module(module):
    print " "


def teardown_module(module):
    print " "


def setup_primes():
    global primes
    primes = primes()
    primes[10]


def setup_squares():
    global squares
    squares = squares()
    squares[25]


def setup_powers():
    #global powers
    pass


def setup_recs():
	""" Uses sequence 1, 3, 4, 7, 11, 18
	"""
    global recs
    global fibs
    recs = recs(0, 1, 3)
    fibs = fibs(0)
    recs[10]
    fibs[10]

def setup_mults():
    global mults
    global mults
    recs = mults(5)
    evens = evens()
    mults[10]
    evens[10]
    
def setup_happys():
    global happys
    happys = happys()
    happys[10]



############# primes test ################

@with_setup(setup_primes)
def test_primes():
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
def test_squares():
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
    powers0[5]
#    assert powers0[0] == 0
    assert powers0[1] == 1
    global powers1
    powers1 = powers(1)
    assert powers1[1] == 1
    assert powers1[2] == 2


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
    
    
############# recs test ##############

@with_setup(setup_recs)
def test_recs():
    assert recs[0] == 1
    assert recs[1] == 3
    assert recs[5] == 18
    assert fibs[0] == 0
    assert fibs[1] == 1
    assert fibs[4] == 3


def test_recs_seq():
    assert recs.seq()[:5] == [1, 3, 4, 7, 11]
    assert fibs.seq()[:9] == [0, 1, 1, 2, 3, 5, 8, 13, 18]


def test_recs_len():
    assert len(recs) == 11
    assert len(fibs) == 11


def test_recs_isa():
    assert recs.isa(3) == True
    assert recs.isa(8) == False
    assert recs.isa(50) == False
    assert fibs.isa(8) == True
    assert fibs.isa(4) == False
    assert fibs.isa(45) == False

@raises(TypeError)
def test_recs_raises_type_error():
    recs[0.5]
    
@raises(TypeError)
def test_fibs_raises_type_error():
    fibs[0.5]
    
############# happys test ############

@with_setup(setup_happys)
def test_happys():
    assert happys[0] == 1
    assert happys[1] == 7
    assert happys[4] == 19


def test_happys_seq():
    assert happys.seq()[:5] == [1, 7, 10, 13, 19]


def test_happys_len():
    assert len(happys) == 11


def test_happys_isa():
    assert happys.isa(7) == True
    assert happys.isa(8) == False
    assert happys.isa(50) == False

@raises(TypeError)
def test_happys_raises_type_error():
    happys[0.5]
    
    
############# mults test ############

@with_setup(setup_mults)
def test_mults():
    assert mults[0] == 0
    assert mults[1] == 5
    assert mults[4] == 20
    assert evens[0] == 0
    assert evens[1] == 2
    assert evens[4] == 6


def test_mults_seq():
    assert mults.seq()[:9] == [0, 5, 10, 15, 20, 25, 30, 35, 40]
	assert evens.seq()[:9] == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_mults_len():
    assert len(mults) == 11
	assert len(evens) == 11

def test_mults_isa():
    assert mults.isa(8) == True
    assert mults.isa(4) == False
    assert mults.isa(45) == False
    assert evens.isa(8) == True
    assert evens.isa(37) == False
    assert evens.isa(63) == False

@raises(TypeError)
def test_mults_raises_type_error():
    mults[0.5]

@raises(TypeError)
def test_evens_raises_type_error():
    mults[0.5]



"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
