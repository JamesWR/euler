"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import util
import math
import pydash as _


def main():
    primes = util.prime_under_list(1000000)
    t_primes = [[2, 3, 5, 7]]
    l_t_primes = [[2, 3, 5, 7]]
    r_t_primes = [[2, 3, 5, 7]]
    i = 0
    while primes[i] < 10:
        i += 1
    size = 2
    while len(t_primes[size - 2]) > 0 or len(t_primes[size - 3]) > 0:
        t_primes.append([])
        r_t_primes.append([])
        l_t_primes.append([])
        while i < len(primes) and primes[i] < (10 ** (size)):
            first_n = primes[i] % (10 ** (size - 1))
            last_n = math.floor(primes[i] / 10)
            is_right_t = first_n in r_t_primes[size - 2]
            is_left_t = last_n in l_t_primes[size - 2]
            if is_right_t and is_left_t:
                t_primes[size - 1].append(primes[i])
                r_t_primes[size - 1].append(primes[i])
                l_t_primes[size - 1].append(primes[i])
            elif is_right_t:
                r_t_primes[size - 1].append(primes[i])
            elif is_left_t:
                l_t_primes[size - 1].append(primes[i])
            i += 1
        size += 1
    print(sum(_.flatten(t_primes[1:])))


if __name__ == "__main__":
    main()
