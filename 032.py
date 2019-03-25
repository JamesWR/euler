"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
import itertools
import pydash as _
import util
import math
import functools


def main():
    result = []
    n_list = list(range(1, 10))
    range_4 = util.orderings(n_list, 4)
    range_1 = util.orderings(n_list[1:], 1)
    range_2 = util.orderings(n_list, 2)
    for i, l_4 in enumerate(range_4):
        num = util.decimal_from_list(l_4)
        found = False
        for l_1 in range_1:
            dev = util.decimal_from_list(l_1)
            nums = functools.reduce(
                lambda x, y: x + y,
                [list(str(num)), list(str(dev)), list(str(int(num / dev))), ["0"]],
            )
            if (
                num % dev == 0
                and math.floor(math.log10(num / dev)) == 3
                and len(nums) == len(set(nums))
            ):
                found = True
                result.append(num)
                break
        if found:
            continue
        for l_2 in range_2:
            dev = util.decimal_from_list(l_2)
            nums = functools.reduce(
                lambda x, y: x + y,
                [list(str(num)), list(str(dev)), list(str(int(num / dev))), ["0"]],
            )
            if (
                num % dev == 0
                and math.floor(math.log10(num / dev)) == 2
                and len(nums) == len(set(nums))
            ):
                result.append(num)
                break
    print(sum(result))

if __name__ == "__main__":
    main()

