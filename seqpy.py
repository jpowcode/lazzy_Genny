from collections import Sequence

class ExpandingSequence(Sequence):
	"""A container class to add methods to the generator functions belo.

    :param Sequence: a function that acts as a generator
    
    :Example:
    
    The following example constructs an object called primes that will
    generate the prime numbers. See ducumentation on primes for examples
    of how to use it.
    
    >>> def primes():
	>>>     return ExpandingSequence(get_primes())
	>>> primes = primes()

    """
    def __init__(self, it):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError
    
		:Example:
    
		Start
    
		>>>

		"""
        self.it = it
        self._cache = []

    def __getitem__(self, index):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError
    
		:Example:
    
		Start
    
		>>>

		"""
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]

    def __len__(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError
    
		:Example:
    
		Start
    
		>>>

		"""
        return len(self._cache)

    def seq(self):
		"""This function does something.

		:param name: The name to use.
		:type name: str.
		:returns:  int -- the return code.
		:raises: AttributeError, KeyError
    
		:Example:
    
		Start
    
		>>>

		"""
		
        return self._cache


def get_primes():
    """Generator to find the prime numbers 
    
    This uses the seive of Erathosens algorithm

    :param None: 
    :returns:  int -- the next prime number in the sequence.
    :raises: AttributeError, KeyError

	:Example:
	
	This is called by using the container function ExpandingSequence
	
	>>> primes = ExpandingSequence(get_primes())
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

def primes():
	"""A wrapper function, creates an object using ExpandingSequence
	class
	"""
	return ExpandingSequence(get_primes())

def get_squares():
    "square numbers"
    candidate = 0
    while True:
        yield candidate*candidate
        candidate +=1

def squares():
	"""A wrapper function, creates an object using ExpandingSequence
	class
	"""
	return ExpandingSequence(get_squares())
	
	
def get_powers(n):
    "Arbitrary powers numbers"
    candidate = 0
    while True:
        yield candidate**n
        candidate +=1
        

def powers(n):
	"""A wrapper function, creates an object using ExpandingSequence
	class
	"""
	return ExpandingSequence(get_powers(n))
	

def get_fibs(n):
    a=0
    b=1
    while True:
        yield a
        a,b,n = b,a+b,n-1
        
def fibs(n):
	return ExpandingSequence(get_fibs(n))
	
def get_recs(n, a, b):
    while True:
        yield a
        a,b,n = b,a+b,n-1
        
def recs(n, a, b):
	return ExpandingSequence(get_recs(n, a, b))

fibs = recs(0, 0, 1)

print fibs[10]
print len(fibs)
print fibs.seq()


