###primes()

Generator to find the prime numbers using the sieve of Erathosenes algorithm.

    :param name: None
    :returns:  int -- the next prime number in the sequence.
    :raises: AttributeError, KeyError

  This is called by using the wrapper function primes() to the
  ExpandingSequence class.

####Example

    >>> primes = primes()
    >>> primes[5]
    >>> primes.seq()
    >>> len(primes)
    11
    [2, 3, 5, 7, 11]
    5
