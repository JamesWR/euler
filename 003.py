"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import util
import pydash as _


def main():
    num = 600851475143
    root = int(num ** (1 / 2))
    primes = util.prime_under_list(root)
    primes.reverse()
    for prime in primes:
        if num % prime == 0:
            print(prime)
            return
    # print(util.prime_factors(600851475143)[-1])


if __name__ == "__main__":
    main()

