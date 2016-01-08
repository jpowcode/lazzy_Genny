from nose import with_setup
from nose.tools import raises
from seqpy import *
from generators import Generators

"""
------------------------------------------------------------------------------
setup and teardown functions
------------------------------------------------------------------------------
"""
G = Generators()

def setup_module(module):
    print " "


def teardown_module(module):
    print " "


def setup_primes():
    global primes
    primes = G.primes()
    primes[10]


def setup_squares():
    global squares
    squares = G.squares()
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
    ndigits[500]


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


def setup_arbfuncs():
    f = lambda n: n**2 + 3*n -1
    global arbfuncs
    global lazcats
    global catnums
    arbfuncs = arbfuncs(f)
    lazcats = lazcats()
    catnums = catnums()
    arbfuncs[10]
    lazcats[10]
    catnums[10]


def setup_mersennes():
    global mersennes
    mersennes = G.mersennes()
    mersennes[10]


def setup_merprimes():
    global merprimes
    merprimes = G.merprimes()
    merprimes[10]


def setup_looksays():
    global looksays
    looksays = looksays()
    looksays[10]


def setup_pis():
    global pis
    pis = pis()
    pis[10]


def setup_harshads():
    global harshads
    harshads = harshads()
    harshads[10]


def setup_consecratios():
    global consecratios
    consecratios = consecratios(happys, 2)
    consecratios[10]


def setup_intersection():
    global intersection
    intersection = intersection(happys, primes)
    intersection[10]


def setup_union():
    global union
    union = union(happys, primes)
    union[10]


def setup_mods():
    global mods
    mods = mods(happys, 3)
    mods[10]


def setup_every():
    global every3
    global every1
    every3 = every(primes, 3)
    every1 = every(primes, 1)
    every3[10]
    every1[10]

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
    assert primes.seq().list()[:7] == [2, 3, 5, 7, 11, 13, 17]


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
    assert squares.seq().list()[:11] == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_squares_between():
    assert squares.seq().between(2, 37).list()[:5] == [4, 9, 16, 25, 36]


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
    assert powers3.seq().list() == [0, 1, 8, 27, 64]


def test_powers_between():
    assert powers3.seq().between(2, 37).list()[:2] == [8, 27]


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
    assert recs.seq().list()[:5] == [1, 3, 4, 7, 11]
    assert fibs.seq().list()[:9] == [0, 1, 1, 2, 3, 5, 8, 13, 21]


def test_recs_between():
    assert recs.seq().between(2, 12).list()[:4] == [3, 4, 7, 11]
    assert fibs.seq().between(5, 13).list()[:3] == [5, 8, 13]


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
    assert happys.seq().list()[:5] == [1, 7, 10, 13, 19]


def test_happys_between():
    assert happys.seq().between(11, 14).list()[:1] == [13]


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
    assert mults.seq().list()[:9] == [0, 5, 10, 15, 20, 25, 30, 35, 40]
    assert evens.seq().list()[:9] == [0, 2, 4, 6, 8, 10, 12, 14, 16]


def test_mults_between():
    assert mults.seq().between(0, 21).list()[:5] == [0, 5, 10, 15, 20]
    assert evens.seq().between(1, 5).list()[:2] == [2, 4]


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
    assert ariths.seq().list()[:6] == [2, 5, 8, 11, 14, 17]
    assert odds.seq().list()[:7] == [1, 3, 5, 7, 9, 11, 13]


def test_ariths_len():
    assert len(ariths) == 11
    assert len(odds) == 11


def test_ariths_between():
    assert ariths.seq().between(12, 18).list() == [14, 17]
    assert odds.seq().between(1, 18).list() == [1, 3, 5, 7, 9, 11, 13, 15, 17]


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
    assert geoms.seq().list()[:6] == [2, 6, 18, 54, 162, 486]


def test_geoms_between():
    assert geoms.seq().between(54, 60).list()[:1] == [54]


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
    assert ndigits.seq().list()[:6] == [100, 101, 102, 103, 104, 105]


def test_ndigits_len():
    assert len(ndigits) == 501


def test_ndigits_between():
    assert ndigits.seq().between(32, 56).list()[:1] == []
    assert ndigits.seq().between(234, 238).list()[:5] == [234, 235, 236, 237, 238]


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
    assert facts.seq().list()[:6] == [1, 1, 2, 6, 24, 120]


def test_facts_between():
    assert facts.seq().between(1, 6).list() == [1, 1, 2, 6]


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
    assert polys.seq().list()[:5] == [1, 5, 12, 22, 35]
    assert triangs.seq().list()[:5] == [1, 3, 6, 10, 15]


def test_polys_between():
    assert polys.seq().between(4, 13).list() == [5, 12]


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
    assert perfs.seq().list()[:3] == [6, 28, 496]
    assert abunds.seq().list()[:4] == [12, 18, 20, 24]
    assert defics.seq().list()[:4] == [1, 2, 3, 4]


def test_perfs_between():
    assert perfs.seq().between(0, 10).list() == [6]
    assert abunds.seq().between(11, 25).list() == [12, 18, 20, 24]
    assert defics.seq().between(3, 6).list() == [3, 4, 5]


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
    assert palinds.seq().list()[:11] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]


def test_palinds_between():
    assert palinds.seq().between(9, 15).list() == [9, 11]


def test_palinds_isa():
    assert palinds.isa(1551) == True
    assert palinds.isa(132) == False
    assert palinds.isa(17) == False


@raises(TypeError)
def test_palinds_raises_type_error():
    palinds[0.5]

"""
------------------------------------------------------------------------------
test arbfuncs and its dpendents
------------------------------------------------------------------------------
"""


@with_setup(setup_arbfuncs)
def test_arbfuncs():
    assert arbfuncs[0] == -1
    assert arbfuncs[1] == 3
    assert arbfuncs[4] == 27
    assert lazcats[0] == 1
    assert lazcats[1] == 2
    assert lazcats[4] == 11
    assert catnums[0] == 1
    assert catnums[1] == 1
    assert catnums[9] == 4862


def test_arbfuncs_len():
    assert len(arbfuncs) == 11
    assert len(lazcats) == 11
    assert len(catnums) == 11


def test_arbfuncs_seq():
    assert arbfuncs.seq().list()[:5] == [-1, 3, 9, 17, 27]
    assert lazcats.seq().list()[:6] == [1, 2, 4, 7, 11, 16]
    assert catnums.seq().list()[:10] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]


def test_arbfuncs_between():
    assert arbfuncs.seq().between(-2, 17).list() == [-1, 3, 9, 17]
    assert lazcats.seq().between(-2, 0).list() == []
    assert catnums.seq().between(2, 1500).list() == [2, 5, 14, 42, 132, 429, 1430]


def test_arbfuncs_isa():
    assert arbfuncs.isa(9) == True
    assert arbfuncs.isa(28) == False
    assert arbfuncs.isa(16) == False
    assert lazcats.isa(11) == True
    assert lazcats.isa(0) == False
    assert lazcats.isa(-4) == False
    assert catnums.isa(132) == True
    assert catnums.isa(18) == False
    assert catnums.isa(500) == False


@raises(TypeError)
def test_arbfuncs_raises_type_error():
    arbfuncs[0.5]


@raises(TypeError)
def test_lazcats_raises_type_error():
    lazcats[0.5]

@raises(TypeError)
def test_catnums_raises_type_error():
    catnums[0.5]


"""
------------------------------------------------------------------------------
test Mersennes
------------------------------------------------------------------------------
"""


@with_setup(setup_mersennes)
def test_mersennes():
    assert mersennes[0] == 0
    assert mersennes[1] == 1
    assert mersennes[4] == 15


def test_mersennes_len():
    assert len(mersennes) == 11


def test_mersennes_seq():
    assert mersennes.seq().list()[:5] == [0, 1, 3, 7, 15]


def test_mersennes_between():
    assert mersennes.seq().between(1, 6).list()[:2] == [1, 3]


def test_mersennes_isa():
    assert mersennes.isa(3) == True
    assert mersennes.isa(5) == False
    assert mersennes.isa(16) == False


@raises(TypeError)
def test_mersennes_raises_type_error():
    mersennes[0.5]


"""
------------------------------------------------------------------------------
test merprimes
------------------------------------------------------------------------------
"""


@with_setup(setup_merprimes)
def test_perimes():
    assert merprimes[0] == 2
    assert merprimes[1] == 3
    assert merprimes[9] == 89

def test_merprimes_len():
    assert len(merprimes) == 11


def test_merprimes_seq():
    assert merprimes.seq().list()[:10] == [2, 3, 5, 7, 13, 17, 19, 31, 61, 89]


def test_merprimes_between():
    assert merprimes.seq().between(-5, 0).list() == []


def test_merprimes_isa():
    assert merprimes.isa(17) == True
    assert merprimes.isa(68) == False
    assert merprimes.isa(259) == False


@raises(TypeError)
def test_merprimes_raises_type_error():
    merprimes[0.5]


"""
------------------------------------------------------------------------------
test looksays
------------------------------------------------------------------------------
"""


@with_setup(setup_looksays)
def test_looksays():
    assert looksays[0] == 1
    assert looksays[1] == 11
    assert looksays[3] == 1211

def test_looksays_len():
    assert len(looksays) == 11


def test_looksays_seq():
    assert looksays.seq().list()[:6] == [1, 11, 21, 1211, 111221, 312211]


def test_looksays_between():
    assert looksays.seq().between(1000, 1500).list() == [1211]


def test_looksays_isa():
    assert looksays.isa(21) == True
    assert looksays.isa(68) == False
    assert looksays.isa(259) == False


@raises(TypeError)
def test_looksays_raises_type_error():
    looksays[0.5]


"""
------------------------------------------------------------------------------
test pis
------------------------------------------------------------------------------
"""


@with_setup(setup_pis)
def test_pis():
    assert pis[0] == 3
    assert pis[1] == 1
    assert pis[3] == 1

def test_pis_len():
    assert len(pis) == 11


def test_pis_seq():
    assert pis.seq().list()[:6] == [3, 1, 4, 1, 5, 9]


# def test_pis_isa():
#     assert pis.isa(2) == True
#     assert pis.isa(68) == False
#     assert pis.isa(0) == False


@raises(TypeError)
def test_pis_raises_type_error():
    pis[0.5]


"""
------------------------------------------------------------------------------
test harshads
------------------------------------------------------------------------------
"""


@with_setup(setup_harshads)
def test_harshads():
    assert harshads[0] == 1
    assert harshads[1] == 2
    assert harshads[10] == 12

def test_harshads_len():
    assert len(harshads) == 11


def test_harshads_seq():
    assert harshads.seq().list()[:7] == [1, 2, 3, 4, 5, 6, 7]



def test_harshads_between():
    assert harshads.seq().between(5, 10).list()[0:6] == [5, 6, 7, 8, 9, 10]


def test_harshads_isa():
    assert harshads.isa(117) == True
    assert harshads.isa(134) == False
    assert harshads.isa(173) == False


@raises(TypeError)
def test_harshads_raises_type_error():
    harshads[0.5]

"""
------------------------------------------------------------------------------
test intersection
------------------------------------------------------------------------------
"""


@with_setup(setup_intersection)
def test_intersection():
    assert intersection[0] == 7
    assert intersection[1] == 13
    assert intersection[3] == 23


def test_intersection_seq():
    assert intersection.seq().list()[0:4] == [7, 13, 19, 23]


"""
------------------------------------------------------------------------------
test union
------------------------------------------------------------------------------
"""


@with_setup(setup_union)
def test_union():
    assert union[0] == 1
    assert union[1] == 2
    assert union[7] == 13

def test_union_seq():
    assert union.seq().list()[:7] == [1, 2, 3, 5, 7, 10, 11]


"""
------------------------------------------------------------------------------
test consecratios
------------------------------------------------------------------------------
"""


@with_setup(setup_consecratios)
def test_consecratio():
    assert consecratios[0] == 7
    assert consecratios[1] == 1.43
    assert consecratios[2] == 1.3

def test_consecratios_seq():
    assert consecratios.seq().list()[:4] == [7, 1.43, 1.3, 1.46]



"""
------------------------------------------------------------------------------
test every
------------------------------------------------------------------------------
"""


@with_setup(setup_every)
def test_every3():
    assert every3[0] == 2
    assert every3[1] == 7
    assert every3[2] == 17

def test_every3_seq():
    assert every3.seq().list()[:4] == [2, 7, 17, 29]


def test_every1():
    assert every1[0] == 2
    assert every1[1] == 3
    assert every1[2] == 5

def test_every1_seq():
    assert every1.seq().list()[:4] == [2, 3, 5, 7]




"""
A generator to make multiple test cases
def test_primes():
    for i in range(1, 5):
        yield check_odd, primes[i]

def check_odd(n):
    assert n % 2 == 1

"""
