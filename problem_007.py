"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from typing import List

def ListPrimes(upper_limit: int) -> List[int]:
    """This uses the Sieve of Eratosthenes ancient algorithm to find
    all prime numbers up to a given limit. With it, one does not need
    to run division tests to find if a number is prime or not.

    More information: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    upper_limit += 1        #Set the upper limit
    not_primes = set()      #Stores not prime numbers
    primes = [2]            #Stores prime numbers

    for maybe_prime in range(3,upper_limit,2):
        """We already know that 2 is the only even prime numbers
        Therefore, we do not need to test any even number.

        If the number is in the not_prime list, we just procced.

        If the number is not in the not_prime list, the number is prime.
        All multiples of the number are stored in the not_prime list and
        the number itself is stored in the prime list.        
        """
        if maybe_prime in not_primes:
            continue
        for not_prime in range(maybe_prime**2, upper_limit, maybe_prime):
            not_primes.add(not_prime)
        primes.append(maybe_prime)
    return primes

def Upper_Limit_Nth_Prime(nth_prime: int) -> int:
    """Finds a well suitable upper limit for the nth_prime number.

    This works because there's a equation that yields a upper limit
    for any nth_prime number, if n > 6. 
    
    More information: https://en.wikipedia.org/wiki/Prime_number_theorem
    """
    from numpy import log   # imports the log function
    if nth_prime < 6:       # the equation works for n > 6
        return 15
    return int(nth_prime * (log(nth_prime) + log(log(nth_prime))))

def Nth_Prime(nth_prime: int) -> int:
    nth_prime -= 1          # Python index starts at zero
    primes = ListPrimes(Upper_Limit_Nth_Prime(nth_prime))
    return primes[nth_prime]

print(Nth_Prime(10001))