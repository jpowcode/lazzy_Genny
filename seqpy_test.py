from nose import with_setup
from nose.tools import raises
from seqpy import *

"""
------------------------------------------------------------------------------
setup and teardown functions
------------------------------------------------------------------------------
"""


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
    global evens
    mults = mults(5)
    evens = evens()
    mults[10]
    evens[10]


def setup_ariths():
    global ariths
    global odds
    ariths = ariths(2, 3)
    odds = odds()
    ariths[10]
    odds[10]


def setup_happys():
    global happys
    happys = happys()
    happys[10]


def setup_geoms():
    global geoms
    geoms = geoms(2, 3)
    geoms[10]


def setup_ndigits():
    global ndigits
    ndigits = ndigits(3)
    ndigits[10]


def setup_facts():
    global facts
    facts = facts()
    facts[10]


def setup_polys():
    global polys
    global triangs
    polys = polys(5)
    triangs = triangs()
    polys[10]
    triangs[10]


def setup_perfs():
    global perfs
    global abunds
    global defics
    perfs = perfs()
    abunds = abunds()
    defics = defics()
    perfs[3]
    abunds[4]
    defics[4]


def setup_palinds():
    global palinds
    palinds = palinds()
    palinds[10]
"""
------------------------------------------------------------------------------
primes test
------------------------------------------------------------------------------
"""


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

"""
------------------------------------------------------------------------------
squares test
------------------------------------------------------------------------------
"""


@with_setup(setup_squares)
def test_squares():
    assert squares[0] == 0
    assert squares[1] == 1
    assert squares[5] == 25


def test_squares_seq():
    assert squares.seq()[:11] == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_squares_between():
    assert squares.between(2, 37) == [4, 9, 16, 25, 36]


def test_squares_len():
    assert len(squares) == 26


def test_squares_isa():
    assert squares.isa(16) == True
    assert squares.isa(13) == False
    assert squares.isa(50) == False


@raises(TypeError)
def test_squares_raises_type_error():
    squares[0.5]

"""
------------------------------------------------------------------------------
powers test
------------------------------------------------------------------------------
"""


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


def test_powers_between():
    assert powers3.between(2, 37) == [8, 27]


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
------------------------------------------------------------------------------
recs test
------------------------------------------------------------------------------
"""


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
    assert fibs.seq()[:9] == [0, 1, 1, 2, 3, 5, 8, 13, 21]


def test_recs_between():
    assert recs.between(2, 12) == [3, 4, 7, 11]
    assert fibs.between(5, 13) == [5, 8, 13]


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


"""
------------------------------------------------------------------------------
happys test
------------------------------------------------------------------------------
"""


@with_setup(setup_happys)
def test_happys():
    assert happys[0] == 1
    assert happys[1] == 7
    assert happys[4] == 19


def test_happys_seq():
    assert happys.seq()[:5] == [1, 7, 10, 13, 19]


def test_happys_between():
    assert happys.between(11, 14) == [13]

def test_happys_len():
    assert len(happys) == 11


def test_happys_isa():
    assert happys.isa(7) == True
    assert happys.isa(8) == False
    assert happys.isa(50) == False


@raises(TypeError)
def test_happys_raises_type_error():
    happys[0.5]

"""
------------------------------------------------------------------------------
mults test
------------------------------------------------------------------------------
"""


@with_setup(setup_mults)
def test_mults():
    assert mults[0] == 0
    assert mults[1] == 5
    assert mults[4] == 20
    assert evens[0] == 0
    assert evens[1] == 2
    assert evens[4] == 8


def test_mults_seq():
    assert mults.seq()[:9] == [0, 5, 10, 15, 20, 25, 30, 35, 40]
    assert evens.seq()[:9] == [0, 2, 4, 6, 8, 10, 12, 14, 16]


def test_mults_between():
    assert mults.between(0, 21) == [0, 5, 10, 15, 20]
    assert evens.between(1, 5) == [2, 4]



def test_mults_len():
    assert len(mults) == 11
    assert len(evens) == 11


def test_mults_isa():
    assert mults.isa(10) == True
    assert mults.isa(4) == False
    assert mults.isa(43) == False
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
------------------------------------------------------------------------------
test ariths and odds
------------------------------------------------------------------------------
"""


@with_setup(setup_ariths)
def test_ariths():
    assert ariths[0] == 2
    assert ariths[1] == 5
    assert ariths[4] == 14
    assert odds[0] == 1
    assert odds[1] == 3
    assert odds[4] == 9


def test_ariths_seq():
    assert ariths.seq()[:6] == [2, 5, 8, 11, 14, 17]
    assert odds.seq()[:7] == [1, 3, 5, 7, 9, 11, 13]

def test_ariths_len():
    assert len(ariths) == 11
    assert len(odds) == 11


def test_ariths_between():
    assert ariths.between(12, 18) == [14, 17]
    assert odds.between(14, 25) == [15, 17, 19, 21, 23, 25]


def test_ariths_isa():
    assert ariths.isa(8) == True
    assert ariths.isa(4) == False
    assert ariths.isa(24) == False
    assert odds.isa(7) == True
    assert odds.isa(2) == False
    assert odds.isa(34) == False


@raises(TypeError)
def test_ariths_raises_type_error():
    ariths[0.5]


@raises(TypeError)
def test_odds_raises_type_error():
    odds[0.5]

"""
------------------------------------------------------------------------------
test geoms
------------------------------------------------------------------------------
"""


@with_setup(setup_geoms)
def test_geoms():
    assert geoms[0] == 2
    assert geoms[1] == 6
    assert geoms[4] == 162


def test_geoms_seq():
    assert geoms.seq()[:6] == [2, 6, 18, 54, 162, 486]


def test_geoms_between():
    assert geoms.between(54, 60) == [54]


def test_geoms_len():
    assert len(geoms) == 11


def test_geoms_isa():
    assert geoms.isa(18) == True
    assert geoms.isa(234) == False
    assert geoms.isa(13) == False


@raises(TypeError)
def test_geoms_raises_type_error():
    geoms[0.5]

"""
------------------------------------------------------------------------------
test ndigits
------------------------------------------------------------------------------
"""


@with_setup(setup_ndigits)
def test_ndigits():
    assert ndigits[0] == 100
    assert ndigits[1] == 101
    assert ndigits[4] == 104


def test_ndigits_seq():
    assert ndigits.seq()[:6] == [100, 101, 102, 103, 104, 105]


def test_ndigits_len():
    assert len(ndigits) == 11


def test_ndigits_between():
    assert ndigits.between(32, 56) == []
    assert ndigits.between(234, 238) == [234, 235, 236, 237, 238]


def test_ndigits_isa():
    assert ndigits.isa(132) == True
    assert ndigits.isa(4590) == False
    assert ndigits.isa(24) == False


@raises(TypeError)
def test_ndigits_raises_type_error():
    ndigits[0.5]

"""
------------------------------------------------------------------------------
test facts
------------------------------------------------------------------------------
"""


@with_setup(setup_facts)
def test_facts():
    assert facts[0] == 1
    assert facts[1] == 1
    assert facts[4] == 24


def test_facts_seq():
    assert facts.seq()[:6] == [1, 1, 2, 6, 24, 120]


def test_facts_between():
    assert facts.between(1, 6) == [1, 1, 2, 6]


def test_facts_len():
    assert len(facts) == 11


def test_facts_isa():
    assert facts.isa(120) == True
    assert facts.isa(132) == False
    assert facts.isa(17) == False


@raises(TypeError)
def test_facts_raises_type_error():
    facts[0.5]

"""
------------------------------------------------------------------------------
test polys and triangs
------------------------------------------------------------------------------
"""


@with_setup(setup_polys)
def test_polys():
    assert polys[0] == 1
    assert polys[1] == 5
    assert polys[3] == 22
    assert triangs[0] == 1
    assert triangs[1] == 3
    assert triangs[4] == 15

def test_polys_seq():
    assert polys.seq()[:5] == [1, 5, 12, 22, 35]
    assert triangs.seq()[:5] == [1, 3, 6, 10, 15]


def test_polys_between():
    assert polys.between(4, 13) == [5, 12]


def test_polys_len():
    assert len(polys) == 11
    assert len(triangs) == 11

def test_polys_isa():
    assert polys.isa(5) == True
    assert polys.isa(23) == False
    assert polys.isa(38) == False
    assert triangs.isa(10) == True
    assert triangs.isa(23) == False
    assert triangs.isa(38) == False

@raises(TypeError)
def test_s_raises_type_error():
    polys[0.5]


@raises(TypeError)
def test_s_raises_type_error():
    triangs[0.5]

"""
------------------------------------------------------------------------------
test perfs and abunds and defics
------------------------------------------------------------------------------
"""


@with_setup(setup_perfs)
def test_perfs():
    assert perfs[0] == 6
    assert perfs[1] == 28
    assert abunds[0] == 12
    assert abunds[1] == 18
    assert abunds[3] == 24
    assert defics[0] == 1
    assert defics[1] == 2
    assert defics[4] == 5

def test_perfs_len():
    assert len(perfs) == 4
    assert len(abunds) == 5
    assert len(defics) == 5


def test_perfs_seq():
    assert perfs.seq()[:3] == [6, 28, 496]
    assert abunds.seq()[:4] == [12, 18, 20, 24]
    assert defics.seq()[:4] == [1, 2, 3, 4]


def test_perfs_between():
    assert perfs.between(0, 10) == [6]
    assert abunds.between(11, 25) == [12, 18, 20, 24]
    assert defics.between(3, 6) == [3, 4, 5]


def test_perfs_isa():
    assert perfs.isa(28) == True
    assert perfs.isa(23) == False
    assert perfs.isa(7) == False
    assert abunds.isa(24) == True
    assert abunds.isa(13) == False
    assert abunds.isa(23) == False
    assert defics.isa(5) == True
    assert defics.isa(6) == False
    assert defics.isa(28) == False

@raises(TypeError)
def test_s_raises_type_error():
    perfs[0.5]


@raises(TypeError)
def test_s_raises_type_error():
    abunds[0.5]


@raises(TypeError)
def test_s_raises_type_error():
    defics[0.5]

"""
------------------------------------------------------------------------------
test palinds
------------------------------------------------------------------------------
"""


@with_setup(setup_palinds)
def test_palinds():
    assert palinds[0] == 1
    assert palinds[1] == 2
    assert palinds[10] == 22

def test_palinds_len():
    assert len(palinds) == 11


def test_palinds_seq():
    assert palinds.seq()[:11] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]


def test_palinds_between():
    assert palinds.between(9, 15) == [9, 11]


def test_palinds_isa():
    assert palinds.isa(1551) == True
    assert palinds.isa(132) == False
    assert palinds.isa(17) == False


@raises(TypeError)
def test_palinds_raises_type_error():
    palinds[0.5]


"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
